# -*- encoding: utf-8 -*-
"""
mobase - Python implementation of Mod Organizer 2's plugin API

This module provides Python interfaces identical to the original C++ mobase library
from Mod Organizer 2, enabling Python plugins to be written without C++ dependencies.

Version: 2.5.2
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from collections.abc import Mapping as ABMapping
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, IntFlag
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    Literal,
    Sequence,
    Type,
    TypeVar,
)

from PySide6.QtCore import (
    QDate,
    QDateTime,
    QDir,
    QFileInfo,
    QLocale,
    QSize,
    Qt,
    QUrl,
)
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QColor, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QMainWindow, QWidget

__version__ = "2.5.2"
INVALID_HANDLE_VALUE = 0xFFFFFFFF
GameFeatureType = TypeVar("GameFeatureType")

# Type alias for MoVariant - represents variant types used in MO2
MoVariant = str | int | float | bool | None


class EndorsedState(Enum):
    """Endorsement state for mods."""

    ENDORSED_FALSE = 0
    ENDORSED_NEVER = 1
    ENDORSED_TRUE = 2
    ENDORSED_UNKNOWN = 3


class GuessQuality(Enum):
    """Describes how good the code considers a guess (e.g., for a mod name)."""

    INVALID = 0
    FALLBACK = 1
    META = 2
    PRESET = 3
    USER = 4
    GOOD = 5


class LoadOrderMechanism(Enum):
    """Load order mechanism used by a game."""

    NONE = 0
    FILE_TIME = 1
    PLUGINS_TXT = 2


class ModState(Enum):
    """State of a mod."""

    EMPTY = 0
    EXISTS = 1
    VALID = 2
    ESSENTIAL = 3
    ENDORSED = 4
    ALTERNATE = 5

    def __and__(self, other: ModState) -> ModState:
        return ModState(self.value & other.value)

    def __or__(self, other: ModState) -> ModState:
        return ModState(self.value | other.value)

    def __xor__(self, other: ModState) -> ModState:
        return ModState(self.value ^ other.value)

    def __invert__(self) -> ModState:
        return ModState(~self.value)


class PluginState(Enum):
    """State of a plugin."""

    MISSING = 0
    INACTIVE = 1
    ACTIVE = 2


class ProfileSetting(IntFlag):
    """Profile settings."""

    MODS = 0
    SAVEGAMES = 1
    CONFIGURATION = 2
    PREFER_DEFAULTS = 3


class ReleaseType(Enum):
    """Release type."""

    PRE_ALPHA = 0
    ALPHA = 1
    BETA = 2
    CANDIDATE = 3
    FINAL = 4


class SortMechanism(Enum):
    """Sort mechanism for a game."""

    NONE = 0
    LOOT = 1
    MLOX = 2
    BOSS = 3


class TrackedState(Enum):
    """Tracked state for mods."""

    TRACKED_UNKNOWN = 0
    TRACKED_FALSE = 1
    TRACKED_TRUE = 2


class VersionScheme(Enum):
    """Version scheme."""

    DISCOVER = 0
    REGULAR = 1
    DECIMAL_MARK = 2
    NUMBERS_AND_LETTERS = 3
    DATE = 4
    LITERAL = 5


class InstallResult(Enum):
    """Result of an installation."""

    NOT_ATTEMPTED = 0
    SUCCESS = 1
    FAILED = 2
    CANCELED = 3
    MANUAL_REQUESTED = 4


@dataclass
class ExecutableForcedLoadSetting:
    """Settings for forced loading libraries for executables."""

    _process: str = field(default="")
    _library: str = field(default="")
    _enabled: bool = field(default=False)
    _forced: bool = field(default=False)

    def enabled(self) -> bool:
        return self._enabled

    def forced(self) -> bool:
        return self._forced

    def library(self) -> str:
        return self._library

    def process(self) -> str:
        return self._process

    def withEnabled(self, enabled: bool) -> ExecutableForcedLoadSetting:
        return ExecutableForcedLoadSetting(
            self._process, self._library, enabled, self._forced
        )

    def withForced(self, forced: bool) -> ExecutableForcedLoadSetting:
        return ExecutableForcedLoadSetting(
            self._process, self._library, self._enabled, forced
        )


@dataclass
class ExecutableInfo:
    """Information about an executable."""

    _title: str
    _binary: QFileInfo
    _arguments: list[str]
    _working_dir: QDir | None
    _steam_app_id: str
    _custom: bool

    def __init__(
        self,
        title: str,
        binary: str | os.PathLike | QFileInfo,
    ):
        self._title = title
        if isinstance(binary, QFileInfo):
            self._binary = binary
        else:
            self._binary = QFileInfo(str(binary))
        self._arguments = []
        self._working_dir = None
        self._steam_app_id = ""
        self._custom = False

    def arguments(self) -> Sequence[str]:
        return self._arguments

    def asCustom(self) -> ExecutableInfo:
        return ExecutableInfo(self._title, self._binary)

    def binary(self) -> QFileInfo:
        return self._binary

    def isCustom(self) -> bool:
        return self._custom

    def isValid(self) -> bool:
        return self._binary.exists()

    def steamAppID(self) -> str:
        return self._steam_app_id

    def title(self) -> str:
        return self._title

    def withArgument(self, argument: str) -> ExecutableInfo:
        new_info = ExecutableInfo(self._title, self._binary)
        new_info._arguments = self._arguments.copy()
        new_info._arguments.append(argument)
        return new_info

    def withSteamAppId(self, app_id: str) -> ExecutableInfo:
        new_info = ExecutableInfo(self._title, self._binary)
        new_info._steam_app_id = app_id
        return new_info

    def withWorkingDirectory(
        self, directory: str | os.PathLike | QDir
    ) -> ExecutableInfo:
        new_info = ExecutableInfo(self._title, self._binary)
        if isinstance(directory, QDir):
            new_info._working_dir = directory
        else:
            new_info._working_dir = QDir(str(directory))
        return new_info


@dataclass
class FileInfo:
    """Information about a virtualized file."""

    archive: str
    filePath: str
    origins: list[str]


@dataclass
class FileMapping:
    """Mapping for virtual file system."""

    source: str
    destination: str
    is_directory: bool
    create_target: bool = False


@dataclass
class ModRepositoryFileInfo:
    """File info from mod repository."""

    gameName: str
    modID: int
    fileID: int
    modName: str = ""
    fileName: str = ""
    version: VersionInfo | None = None
    newestVersion: VersionInfo | None = None
    fileTime: QDateTime | None = None
    fileSize: int = 0
    description: str = ""
    fileCategory: int = 0
    categoryID: int = 0
    repository: str = ""
    uri: str = ""
    userData: MoVariant = None

    @staticmethod
    def createFromJson(data: str) -> ModRepositoryFileInfo:
        import json

        parsed = json.loads(data)
        info = ModRepositoryFileInfo(
            gameName=parsed.get("gameName", ""),
            modID=parsed.get("modID", 0),
            fileID=parsed.get("fileID", 0),
        )
        if "modName" in parsed:
            info.modName = parsed["modName"]
        if "fileName" in parsed:
            info.fileName = parsed["fileName"]
        if "version" in parsed:
            info.version = VersionInfo(parsed["version"])
        if "newestVersion" in parsed:
            info.newestVersion = VersionInfo(parsed["newestVersion"])
        if "fileTime" in parsed:
            info.fileTime = QDateTime.fromString(parsed["fileTime"], Qt.ISODate)
        if "fileSize" in parsed:
            info.fileSize = parsed["fileSize"]
        if "description" in parsed:
            info.description = parsed["description"]
        if "fileCategory" in parsed:
            info.fileCategory = parsed["fileCategory"]
        if "categoryID" in parsed:
            info.categoryID = parsed["categoryID"]
        if "repository" in parsed:
            info.repository = parsed["repository"]
        if "uri" in parsed:
            info.uri = parsed["uri"]
        if "userData" in parsed:
            info.userData = parsed["userData"]
        return info


@dataclass
class PluginSetting:
    """User-configurable parameter for a plugin."""

    key: str
    description: str
    default_value: MoVariant


class VersionInfo:
    """Represents the version of a mod or plugin."""

    def __init__(
        self,
        value: str | None = None,
        scheme: VersionScheme = VersionScheme.DISCOVER,
        major: int = 0,
        minor: int = 0,
        subminor: int = 0,
        subsubminor: int = 0,
        release_type: ReleaseType = ReleaseType.FINAL,
    ):
        self._scheme = scheme
        self._major = major
        self._minor = minor
        self._subminor = subminor
        self._subsubminor = subsubminor
        self._release_type = release_type
        self._valid = False

        if value is not None:
            self.parse(value, scheme)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, VersionInfo):
            return False
        return (
            self._major == other._major
            and self._minor == other._minor
            and self._subminor == other._subminor
            and self._subsubminor == other._subsubminor
            and self._release_type == other._release_type
        )

    def __lt__(self, other: VersionInfo) -> bool:
        if self._major != other._major:
            return self._major < other._major
        if self._minor != other._minor:
            return self._minor < other._minor
        if self._subminor != other._subminor:
            return self._subminor < other._subminor
        if self._subsubminor != other._subsubminor:
            return self._subsubminor < other._subsubminor
        return self._release_type.value < other._release_type.value

    def __le__(self, other: VersionInfo) -> bool:
        return self == other or self < other

    def __gt__(self, other: VersionInfo) -> bool:
        return not self <= other

    def __ge__(self, other: VersionInfo) -> bool:
        return not self < other

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __str__(self) -> str:
        return self.canonicalString()

    def canonicalString(self) -> str:
        """Returns a canonical string representing this version."""
        if not self._valid:
            return ""
        parts = [str(self._major)]
        if self._minor > 0 or self._subminor > 0 or self._subsubminor > 0:
            parts.append(str(self._minor))
        if self._subminor > 0 or self._subsubminor > 0:
            parts.append(str(self._subminor))
        if self._subsubminor > 0:
            parts.append(str(self._subsubminor))
        if self._release_type != ReleaseType.FINAL:
            parts.append(self._release_type.name)
        return ".".join(parts)

    def clear(self) -> None:
        """Resets this VersionInfo to an invalid version."""
        self._major = 0
        self._minor = 0
        self._subminor = 0
        self._subsubminor = 0
        self._release_type = ReleaseType.FINAL
        self._valid = False

    def displayString(self, forced_segments: int = 2) -> str:
        """Returns a string for display to the user."""
        if not self._valid:
            return "Unknown"
        if forced_segments == 2:
            return f"{self._major}.{self._minor}"
        elif forced_segments == 3:
            return f"{self._major}.{self._minor}.{self._subminor}"
        elif forced_segments >= 4:
            return self.canonicalString()
        else:
            return str(self._major)

    def isValid(self) -> bool:
        """Returns True if this VersionInfo is valid, False otherwise."""
        return self._valid

    def parse(
        self,
        value: str,
        scheme: VersionScheme = VersionScheme.DISCOVER,
        is_manual: bool = False,
    ) -> None:
        """Update this VersionInfo by parsing the given string using the given scheme."""
        self._scheme = scheme
        self._valid = False

        if not value:
            return

        value = value.strip()
        if scheme == VersionScheme.DISCOVER:
            self._parseDiscover(value, is_manual)
        elif scheme == VersionScheme.REGULAR:
            self._parseRegular(value)
        else:
            # For other schemes, try to parse as regular
            self._parseRegular(value)

    def _parseDiscover(self, value: str, is_manual: bool) -> None:
        """Parse using DISCOVER scheme."""
        # Simple regex-based parsing for version strings
        import re

        # Match version pattern like "1.2.3" or "1.2.3-beta"
        match = re.match(r"^(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(\d+))?", value)
        if match:
            self._major = int(match.group(1))
            if match.group(2):
                self._minor = int(match.group(2))
            if match.group(3):
                self._subminor = int(match.group(3))
            if match.group(4):
                self._subsubminor = int(match.group(4))

            # Check for release type
            lower_value = value.lower()
            if "alpha" in lower_value:
                self._release_type = ReleaseType.ALPHA
            elif "beta" in lower_value:
                self._release_type = ReleaseType.BETA
            elif "rc" in lower_value or "candidate" in lower_value:
                self._release_type = ReleaseType.CANDIDATE

            self._valid = True

    def _parseRegular(self, value: str) -> None:
        """Parse using REGULAR scheme (major.minor.subminor.subsubminor)."""
        parts = value.split(".")
        if len(parts) >= 1:
            try:
                self._major = int(parts[0])
                self._valid = True
            except ValueError:
                pass
        if len(parts) >= 2:
            try:
                self._minor = int(parts[1])
            except ValueError:
                pass
        if len(parts) >= 3:
            try:
                self._subminor = int(parts[2])
            except ValueError:
                pass
        if len(parts) >= 4:
            try:
                self._subsubminor = int(parts[3])
            except ValueError:
                pass

    def scheme(self) -> VersionScheme:
        """Returns the version scheme in effect for this VersionInfo."""
        return self._scheme


class GuessedString:
    """Represents a string that may be set from different places."""

    def __init__(self, value: str, quality: GuessQuality = GuessQuality.USER):
        self._value = value
        self._quality = quality
        self._filter: Callable[[str], str | bool] | None = None
        self._variants: set[str] = set()

    def __str__(self) -> str:
        return self._value

    def reset(
        self,
        value: str | GuessedString | None = None,
        quality: GuessQuality | None = None,
    ) -> GuessedString:
        """Reset this GuessedString object by copying the given one."""
        if value is None:
            return self

        if isinstance(value, GuessedString):
            if value._quality.value > self._quality.value:
                self._value = value._value
                self._quality = value._quality
                self._variants.add(value._value)
        else:
            if quality is not None and quality.value > self._quality.value:
                self._value = value
                self._quality = quality
                self._variants.add(value)

        return self

    def setFilter(self, filter: Callable[[str], str | bool]) -> None:
        """Set the filter for this GuessedString."""
        self._filter = filter

    def update(self, value: str, quality: GuessQuality | None = None) -> GuessedString:
        """Update this GuessedString by adding a new variant with the given quality."""
        if quality is None:
            quality = GuessQuality.USER

        # Apply filter if set
        if self._filter is not None:
            try:
                filtered = self._filter(value)
                if filtered is False:
                    return self
                elif isinstance(filtered, str):
                    value = filtered
            except Exception:
                return self

        self._variants.add(value)
        if quality.value > self._quality.value:
            self._value = value
            self._quality = quality

        return self

    def variants(self) -> set[str]:
        """Returns the list of variants for this GuessedString."""
        return self._variants


class GameFeature(ABC):
    """Base class for all game features, cannot be inherited, used only for typing."""


class BSAInvalidation(GameFeature):
    """BSA Invalidation game feature."""

    @abstractmethod
    def activate(self, profile: IProfile) -> None: ...

    @abstractmethod
    def deactivate(self, profile: IProfile) -> None: ...

    @abstractmethod
    def isInvalidationBSA(self, name: str) -> bool: ...


class DataArchives(GameFeature):
    """Data Archives game feature."""

    @abstractmethod
    def addArchive(self, profile: IProfile, index: int, name: str) -> None:
        """Add an archive to the archive list."""
        ...

    @abstractmethod
    def archives(self, profile: IProfile) -> Sequence[str]:
        """Retrieve the list of archives in the given profile."""
        ...

    @abstractmethod
    def removeArchive(self, profile: IProfile, name: str) -> None:
        """Remove the given archive from the given profile."""
        ...

    @abstractmethod
    def vanillaArchives(self) -> Sequence[str]:
        """Retrieve the list of vanilla archives."""
        ...


class GamePlugins(GameFeature):
    """Game Plugins game feature."""

    @abstractmethod
    def getLoadOrder(self) -> Sequence[str]: ...

    @abstractmethod
    def lightPluginsAreSupported(self) -> bool:
        """Returns True if light plugins are supported, False otherwise."""
        ...

    @abstractmethod
    def mediumPluginsAreSupported(self) -> bool:
        """Returns True if medium plugins are supported, False otherwise."""
        ...

    @abstractmethod
    def readPluginLists(self, plugin_list: IPluginList) -> None: ...

    @abstractmethod
    def writePluginLists(self, plugin_list: IPluginList) -> None: ...


class LocalSavegames(GameFeature):
    """Local Savegames game feature."""

    @abstractmethod
    def mappings(self, profile_save_dir: QDir) -> list[FileMapping]: ...

    @abstractmethod
    def prepareProfile(self, profile: IProfile) -> bool: ...


class ModDataContent(GameFeature):
    """Mod Data Content game feature."""

    class Content:
        """Content item for ModDataContent."""

        def __init__(self, id: int, name: str, icon: str, filter_only: bool = False):
            self._id = id
            self._name = name
            self._icon = icon
            self._filter_only = filter_only

        def id(self) -> int:
            return self._id

        def name(self) -> str:
            return self._name

        def icon(self) -> str:
            return self._icon

        def isOnlyForFilter(self) -> bool:
            return self._filter_only

    @abstractmethod
    def getAllContents(self) -> list[ModDataContent.Content]: ...

    @abstractmethod
    def getContentsFor(self, filetree: IFileTree) -> list[int]: ...


class SaveGameInfo(GameFeature):
    """Save Game Info game feature."""

    @abstractmethod
    def getMissingAssets(self, save: ISaveGame) -> Dict[str, Sequence[str]]: ...

    @abstractmethod
    def getSaveGameWidget(self, parent: QWidget) -> ISaveGameInfoWidget | None: ...


class ScriptExtender(GameFeature):
    """Script Extender game feature."""

    @abstractmethod
    def binaryName(self) -> str:
        """Returns the name of the script extender binary."""
        ...

    @abstractmethod
    def getArch(self) -> int:
        """Returns the CPU platform of the extender."""
        ...

    @abstractmethod
    def getExtenderVersion(self) -> str:
        """Returns the version of the script extender."""
        ...

    @abstractmethod
    def isInstalled(self) -> bool:
        """Returns True if the script extender is installed, False otherwise."""
        ...

    @abstractmethod
    def loaderName(self) -> str:
        """Returns the loader to use to ensure the game runs with the script extender."""
        ...

    @abstractmethod
    def loaderPath(self) -> str | os.PathLike | QFileInfo:
        """Returns the full path to the script extender loader."""
        ...

    @abstractmethod
    def pluginPath(self) -> str | os.PathLike | QDir:
        """Returns the script extender plugin path, relative to the data folder."""
        ...

    @abstractmethod
    def savegameExtension(self) -> str:
        """Retrieve the extension of script extender save files."""
        ...


class UnmanagedMods(GameFeature):
    """Unmanaged Mods game feature."""

    @abstractmethod
    def displayName(self, mod_name: str) -> str:
        """Retrieve the display name of a given mod."""
        ...

    @abstractmethod
    def mods(self, official_only: bool) -> Sequence[str]:
        """Retrieve the list of unmanaged mods for the corresponding game."""
        ...

    @abstractmethod
    def referenceFile(self, mod_name: str) -> str | os.PathLike | QFileInfo:
        """Retrieve the reference file for the requested mod."""
        ...

    @abstractmethod
    def secondaryFiles(self, mod_name: str) -> Sequence[str | os.PathLike | QFileInfo]:
        """Retrieve the secondary files for the requested mod."""
        ...


class FileTreeEntry:
    """Represent an entry in a file tree, either a file or a directory."""

    class FileTypes(Enum):
        """Enumeration of the different file type or combinations."""

        FILE = 1
        DIRECTORY = 2
        FILE_OR_DIRECTORY = 3

    def __init__(self):
        self._name: str = ""
        self._parent: IFileTree | None = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FileTreeEntry):
            return False
        return self._name == other._name

    def detach(self) -> bool:
        """Detach this entry from its parent tree."""
        if self._parent is None:
            return False
        return self._parent.remove(self)

    def fileType(self) -> FileTreeEntry.FileTypes:
        """Returns the filetype of this entry."""
        raise NotImplementedError("fileType must be implemented by subclass")

    def hasSuffix(self, *suffixes: str) -> bool:
        """Check if this entry has the given suffix(es)."""
        if not self.isFile():
            return False
        name_lower = self._name.lower()
        for suffix in suffixes:
            if name_lower.endswith(suffix.lower()):
                return True
        return False

    def isDir(self) -> bool:
        """Returns True if this entry is a directory, False otherwise."""
        return self.fileType() == FileTreeEntry.FileTypes.DIRECTORY

    def isFile(self) -> bool:
        """Returns True if this entry is a file, False otherwise."""
        return self.fileType() == FileTreeEntry.FileTypes.FILE

    def moveTo(self, tree: IFileTree) -> bool:
        """Move this entry to the given tree."""
        if self._parent is None:
            return False
        return self._parent.move(self, "", IFileTree.InsertPolicy.FAIL_IF_EXISTS)

    def name(self) -> str:
        """Returns the name of this entry."""
        return self._name

    def parent(self) -> IFileTree | None:
        """Returns the parent tree containing this entry, or None."""
        return self._parent

    def path(self, sep: str = "\\") -> str:
        """Retrieve the path from this entry up to the root of the tree."""
        parts = [self._name]
        current = self._parent
        while current is not None:
            parts.insert(0, current._name)
            current = current.parent()
        return sep.join(parts)

    def pathFrom(self, tree: IFileTree, sep: str = "\\") -> str:
        """Retrieve the path from the given tree to this entry."""
        if self._parent is None:
            return ""

        if self._parent == tree:
            return self._name

        parent_path = self._parent.pathFrom(tree, sep)
        if parent_path:
            return parent_path + sep + self._name
        return ""

    def suffix(self) -> str:
        """Retrieve the 'last' extension of this entry."""
        if not self.isFile():
            return ""
        parts = self._name.rsplit(".", 1)
        return parts[1] if len(parts) > 1 else ""

    DIRECTORY = FileTypes.DIRECTORY
    FILE = FileTypes.FILE
    FILE_OR_DIRECTORY = FileTypes.FILE_OR_DIRECTORY


class IFileTree(FileTreeEntry):
    """Interface to classes that provides way to visualize and alter file trees."""

    class InsertPolicy(Enum):
        """Policy for inserting entries."""

        FAIL_IF_EXISTS = 0
        REPLACE = 1
        MERGE = 2

    class WalkReturn(Enum):
        """Enumeration that can be returned by the callback for the walk() method."""

        CONTINUE = 0
        SKIP = 1
        STOP = 2

    def __init__(self, name: str = ""):
        super().__init__()
        self._name = name
        self._entries: list[FileTreeEntry] = []

    def __bool__(self) -> bool:
        """Returns True if this tree is not empty, False otherwise."""
        return len(self._entries) > 0

    def __getitem__(self, index: int) -> FileTreeEntry:
        """Retrieve the entry at the given index in this tree."""
        return self._entries[index]

    def __iter__(self) -> Iterator[IFileTree | FileTreeEntry]:
        """Retrieves an iterator for entries directly under this tree."""
        return iter(self._entries)

    def __len__(self) -> int:
        """Returns the number of entries directly under this tree."""
        return len(self._entries)

    def addDirectory(self, path: str) -> IFileTree:
        """Create a new directory tree under this tree."""
        raise NotImplementedError("addDirectory must be implemented by subclass")

    def addFile(self, path: str, replace_if_exists: bool = False) -> FileTreeEntry:
        """Create a new file directly under this tree."""
        raise NotImplementedError("addFile must be implemented by subclass")

    def clear(self) -> bool:
        """Delete (detach) all the entries from this tree."""
        removed = 0
        for entry in list(self._entries):
            if entry.detach():
                removed += 1
            else:
                break
        return removed == len(self._entries)

    def copy(
        self,
        entry: FileTreeEntry,
        path: str = "",
        insert_policy: InsertPolicy = InsertPolicy.FAIL_IF_EXISTS,
    ) -> FileTreeEntry:
        """Move the given entry to the given path under this tree."""
        raise NotImplementedError("copy must be implemented by subclass")

    def createOrphanTree(self, name: str = "") -> IFileTree:
        """Create a new orphan empty tree."""
        raise NotImplementedError("createOrphanTree must be implemented by subclass")

    def exists(
        self,
        path: str,
        type: FileTreeEntry.FileTypes = FileTreeEntry.FileTypes.FILE_OR_DIRECTORY,
    ) -> bool:
        """Check if the given entry exists."""
        entry = self.find(path, type)
        return entry is not None

    def find(
        self,
        path: str,
        type: FileTreeEntry.FileTypes = FileTreeEntry.FileTypes.FILE_OR_DIRECTORY,
    ) -> IFileTree | FileTreeEntry | None:
        """Retrieve the given entry."""
        raise NotImplementedError("find must be implemented by subclass")

    def insert(
        self, entry: FileTreeEntry, policy: InsertPolicy = InsertPolicy.FAIL_IF_EXISTS
    ) -> bool:
        """Insert the given entry in this tree, removing it from its previous parent."""
        raise NotImplementedError("insert must be implemented by subclass")

    def merge(
        self, other: IFileTree, overwrites: bool = False
    ) -> Dict[FileTreeEntry, FileTreeEntry] | int:
        """Merge the given tree with this tree."""
        raise NotImplementedError("merge must be implemented by subclass")

    def move(
        self,
        entry: FileTreeEntry,
        path: str,
        policy: InsertPolicy = InsertPolicy.FAIL_IF_EXISTS,
    ) -> bool:
        """Move the given entry to the given path under this tree."""
        raise NotImplementedError("move must be implemented by subclass")

    def pathTo(self, entry: FileTreeEntry, sep: str = "\\") -> str:
        """Retrieve the path from this tree to the given entry."""
        if entry._parent == self:
            return entry._name

        current = entry._parent
        parts = [entry._name]
        while current is not None and current != self:
            parts.insert(0, current._name)
            current = current.parent()

        if current != self:
            return ""

        return sep.join(parts)

    def remove(self, name: str | FileTreeEntry) -> bool:
        """Delete the given entry."""
        if isinstance(name, FileTreeEntry):
            entry = name
        else:
            entry = None
            for e in self._entries:
                if e._name == name:
                    entry = e
                    break

        if entry is None or entry not in self._entries:
            return False

        entry._parent = None
        self._entries.remove(entry)
        return True

    def removeAll(self, names: Sequence[str]) -> int:
        """Delete the entries with the given names from the tree."""
        removed = 0
        for name in names:
            if self.remove(name):
                removed += 1
        return removed

    def removeIf(self, filter: Callable[[FileTreeEntry], bool]) -> int:
        """Delete entries matching the given predicate from the tree."""
        removed = 0
        for entry in list(self._entries):
            if filter(entry):
                if self.remove(entry):
                    removed += 1
        return removed

    def walk(
        self,
        callback: Callable[[str, FileTreeEntry, IFileTree], WalkReturn],
        sep: str = "\\",
    ) -> None:
        """Walk this tree, calling the given function for each entry in it."""

        def walk_recursive(tree: IFileTree, current_path: str) -> IFileTree.WalkReturn:
            for entry in tree:
                result = callback(current_path, entry, tree)
                if result == IFileTree.WalkReturn.STOP:
                    return result
                if result == IFileTree.WalkReturn.SKIP:
                    continue

                if entry.isDir():
                    new_path = (
                        current_path + sep + entry._name
                        if current_path
                        else entry._name
                    )
                    result = walk_recursive(entry, new_path)  # type: ignore[arg-type]
                    if result == IFileTree.WalkReturn.STOP:
                        return result

            return IFileTree.WalkReturn.CONTINUE

        walk_recursive(self, "")

    CONTINUE = WalkReturn.CONTINUE
    FAIL_IF_EXISTS = InsertPolicy.FAIL_IF_EXISTS
    MERGE = InsertPolicy.MERGE
    REPLACE = InsertPolicy.REPLACE
    SKIP = WalkReturn.SKIP
    STOP = WalkReturn.STOP


class IPlugin(ABC):
    """Base class for all plugins."""

    @abstractmethod
    def author(self) -> str:
        """Returns the name of the plugin author."""
        ...

    @abstractmethod
    def description(self) -> str:
        """Returns the description for this plugin."""
        ...

    def enabledByDefault(self) -> bool:
        """Check whether this plugin should be enabled by default."""
        return False

    @abstractmethod
    def init(self, organizer: IOrganizer) -> bool:
        """Initialize this plugin."""
        ...

    def localizedName(self) -> str:
        """Retrieve the localized name of the plugin."""
        return self.name()

    def master(self) -> str:
        """Retrieve the master plugin of this plugin."""
        return ""

    @abstractmethod
    def name(self) -> str:
        """Retrieve the name of the plugin."""
        ...

    def requirements(self) -> list[IPluginRequirement]:
        """Retrieve the requirements for this plugin."""
        return []

    @abstractmethod
    def settings(self) -> Sequence[PluginSetting]:
        """Returns a list of settings for this plugin."""
        ...

    @abstractmethod
    def version(self) -> VersionInfo:
        """Returns the version of this plugin."""
        ...

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls._organizer: IOrganizer | None = None


class ISaveGame(ABC):
    """Base class for information about what is in a save game."""

    def allFiles(self) -> Sequence[str | os.PathLike | QFileInfo]:
        """Returns the list of all files related to this save."""
        return []

    @abstractmethod
    def getCreationTime(self) -> QDateTime:
        """Retrieve the creation time of the save."""
        ...

    @abstractmethod
    def getFilepath(self) -> str | os.PathLike | QFileInfo:
        """Returns the path name to the (main) file or folder for the save."""
        ...

    @abstractmethod
    def getName(self) -> str:
        """Returns the name of this save, for display purpose."""
        ...

    @abstractmethod
    def getSaveGroupIdentifier(self) -> str:
        """Retrieve the name of the group this files belong to."""
        ...

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)


class ISaveGameInfoWidget(QWidget):
    """Base class for a save game info widget."""

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

    @abstractmethod
    def setSave(self, save: ISaveGame) -> None:
        """Set the save file to display in this widget."""
        ...

    def _widget(self) -> QWidget:
        """Returns the underlying QWidget."""
        return self


class ModDataChecker(GameFeature):
    """Game feature that is used to check the content of a data tree."""

    class CheckReturn(Enum):
        """Return value for dataLooksValid."""

        INVALID = 0
        FIXABLE = 1
        VALID = 2

    @abstractmethod
    def dataLooksValid(self, filetree: IFileTree) -> ModDataChecker.CheckReturn:
        """Check that the given filetree represent a valid mod layout."""
        ...

    @abstractmethod
    def fix(self, filetree: IFileTree) -> IFileTree | None:
        """Try to fix the given tree."""
        ...

    FIXABLE = CheckReturn.FIXABLE
    INVALID = CheckReturn.INVALID
    VALID = CheckReturn.VALID


class IPluginRequirement:
    """Class representing requirements for plugins."""

    class Problem:
        """Class representing a problem found by a requirement."""

        def __init__(self, short_description: str, long_description: str = ""):
            self._short = short_description
            self._long = long_description

        def longDescription(self) -> str:
            """Returns a long description of the problem."""
            return self._long

        def shortDescription(self) -> str:
            """Returns a short description of the problem."""
            return self._short

    def check(self, organizer: IOrganizer) -> IPluginRequirement.Problem | None:
        """Check if the requirement is met, and return a problem if not."""
        raise NotImplementedError("check must be implemented by subclass")


class PluginRequirementFactory:
    """Factory for creating plugin requirements."""

    @staticmethod
    def basic(
        checker: Callable[[IOrganizer], bool], description: str
    ) -> IPluginRequirement:
        """Create a basic requirement."""

        class BasicRequirement(IPluginRequirement):
            def __init__(self, _checker, _description):
                self._checker = _checker
                self._description = _description

            def check(self, organizer: IOrganizer) -> IPluginRequirement.Problem | None:
                if not self._checker(organizer):
                    return IPluginRequirement.Problem(self._description)
                return None

        return BasicRequirement(checker, description)

    @staticmethod
    def diagnose(diagnose: IPluginDiagnose) -> IPluginRequirement:
        """Construct a requirement from a diagnose plugin."""

        class DiagnoseRequirement(IPluginRequirement):
            def __init__(self, _diagnose):
                self._diagnose = _diagnose

            def check(self, organizer: IOrganizer) -> IPluginRequirement.Problem | None:
                problems = self._diagnose.activeProblems()
                if problems:
                    return IPluginRequirement.Problem(
                        self._diagnose.shortDescription(problems[0]),
                        self._diagnose.fullDescription(problems[0]),
                    )
                return None

        return DiagnoseRequirement(diagnose)

    @staticmethod
    def gameDependency(*games: str) -> IPluginRequirement:
        """Create a new game dependency requirement."""

        class GameDependencyRequirement(IPluginRequirement):
            def __init__(self, _games):
                self._games = games if isinstance(games, (list, tuple)) else (games,)

            def check(self, organizer: IOrganizer) -> IPluginRequirement.Problem | None:
                if organizer.managedGame() is None:
                    return None
                game_name = organizer.managedGame().gameName()
                if game_name not in self._games:
                    return IPluginRequirement.Problem(
                        f"Game '{game_name}' is not supported. "
                        f"Required: {', '.join(self._games)}"
                    )
                return None

        return GameDependencyRequirement(games)

    @staticmethod
    def pluginDependency(*plugins: str) -> IPluginRequirement:
        """Create a new plugin dependency requirement."""

        class PluginDependencyRequirement(IPluginRequirement):
            def __init__(self, _plugins):
                self._plugins = (
                    plugins if isinstance(plugins, (list, tuple)) else (plugins,)
                )

            def check(self, organizer: IOrganizer) -> IPluginRequirement.Problem | None:
                for plugin_name in self._plugins:
                    if not organizer.isPluginEnabled(plugin_name):
                        return IPluginRequirement.Problem(
                            f"Plugin '{plugin_name}' is required but not enabled"
                        )
                return None

        return PluginDependencyRequirement(plugins)


class IPluginDiagnose(IPlugin):
    """Plugins that create problem reports to be displayed in the UI."""

    def _invalidate(self) -> None:
        """Invalidate the problems corresponding to this plugin."""
        pass

    @abstractmethod
    def activeProblems(self) -> list[int]:
        """Retrieve the list of active problems found by this plugin."""
        ...

    @abstractmethod
    def fullDescription(self, key: int) -> str:
        """Retrieve the full description of the problem corresponding to the given key."""
        ...

    @abstractmethod
    def hasGuidedFix(self, key: int) -> bool:
        """Check if the problem corresponding to the given key has a guided fix."""
        ...

    @abstractmethod
    def shortDescription(self, key: int) -> str:
        """Retrieve the short description of the problem corresponding to the given key."""
        ...

    @abstractmethod
    def startGuidedFix(self, key: int) -> None:
        """Starts a guided fix for the problem corresponding to the given key."""
        ...


class IPluginFileMapper(IPlugin):
    """Plugins that adds virtual file links."""

    @abstractmethod
    def mappings(self) -> list[FileMapping]:
        """Returns mapping for the virtual file system (VFS)."""
        ...


class IPluginInstaller(IPlugin):
    """This is the top-level class for installer."""

    def _manager(self) -> IInstallationManager:
        """Returns the installation manager."""
        raise NotImplementedError("_manager must be implemented by subclass")

    def _parentWidget(self) -> QWidget:
        """Returns the parent widget."""
        raise NotImplementedError("_parentWidget must be implemented by subclass")

    @abstractmethod
    def isArchiveSupported(self, tree: IFileTree) -> bool:
        """Check if the given file tree corresponds to a supported archive."""
        ...

    @abstractmethod
    def isManualInstaller(self) -> bool:
        """Check if this installer is a manual installer."""
        ...

    def onInstallationEnd(
        self, result: InstallResult, new_mod: IModInterface | None
    ) -> None:
        """Method calls at the end of the installation process."""
        pass

    def onInstallationStart(
        self, archive: str, reinstallation: bool, current_mod: IModInterface | None
    ) -> None:
        """Method calls at the start of the installation process."""
        pass

    @abstractmethod
    def priority(self) -> int:
        """Retrieve the priority of this installer."""
        ...

    def setInstallationManager(self, manager: IInstallationManager) -> None:
        """Set the installation manager for this installer."""
        raise NotImplementedError(
            "setInstallationManager must be implemented by subclass"
        )

    def setParentWidget(self, parent: QWidget) -> None:
        """Set the parent widget for this installer."""
        raise NotImplementedError("setParentWidget must be implemented by subclass")


class IPluginInstallerCustom(IPluginInstaller):
    """Custom installer for mods."""

    @abstractmethod
    def install(
        self,
        mod_name: GuessedString,
        game_name: str,
        archive_name: str,
        version: str,
        nexus_id: int,
    ) -> InstallResult:
        """Install the given archive."""
        ...

    @abstractmethod
    def isArchiveSupported(self, archive_name: str) -> bool:
        """Check if the given file is a supported archive."""
        ...

    @abstractmethod
    def supportedExtensions(self) -> set[str]:
        """Returns a list of file extensions that this installer can handle."""
        ...


class IPluginInstallerSimple(IPluginInstaller):
    """Simple installer for mods."""

    @abstractmethod
    def install(
        self, name: GuessedString, tree: IFileTree, version: str, nexus_id: int
    ) -> InstallResult | IFileTree | tuple[InstallResult, IFileTree, str, int]:
        """Install a mod from an archive filetree."""
        ...


class IPluginModPage(IPlugin):
    """Base class for all plugins."""

    def _parentWidget(self) -> QWidget:
        """Returns the parent widget."""
        raise NotImplementedError("_parentWidget must be implemented by subclass")

    @abstractmethod
    def displayName(self) -> str:
        """Returns the name of the page as displayed in the UI."""
        ...

    @abstractmethod
    def handlesDownload(
        self, page_url: QUrl, download_url: QUrl, fileinfo: ModRepositoryFileInfo
    ) -> bool:
        """Check if the plugin handles the specified download."""
        ...

    @abstractmethod
    def icon(self) -> QIcon:
        """Returns the icon to display with the page."""
        ...

    @abstractmethod
    def pageURL(self) -> QUrl:
        """Returns the URL to open when the user wants to visit this mod page."""
        ...

    def setParentWidget(self, parent: QWidget) -> None:
        """Set the parent widget for this mod page."""
        raise NotImplementedError("setParentWidget must be implemented by subclass")

    @abstractmethod
    def useIntegratedBrowser(self) -> bool:
        """Indicates if the page should be displayed in the integrated browser."""
        ...


class IPluginPreview(IPlugin):
    """These plugins add support for previewing files in the data pane."""

    @abstractmethod
    def genDataPreview(
        self, file_data: QByteArray, filename: str, max_size: QSize
    ) -> QWidget:
        """Generate a preview widget from in-memory data."""
        ...

    @abstractmethod
    def genFilePreview(self, filename: str, max_size: QSize) -> QWidget:
        """Generate a preview widget for the specified file."""
        ...

    @abstractmethod
    def supportedExtensions(self) -> set[str]:
        """Returns the list of file extensions that are supported by this preview plugin."""
        ...

    @abstractmethod
    def supportsArchives(self) -> bool:
        """Check if this preview plugin supports preview from in-memory data."""
        ...


class IPluginTool(IPlugin):
    """This is the simplest of plugin interfaces."""

    def _parentWidget(self) -> QWidget:
        """Returns the parent widget."""
        raise NotImplementedError("_parentWidget must be implemented by subclass")

    @abstractmethod
    def display(self) -> None:
        """Called when the user starts the tool."""
        ...

    @abstractmethod
    def displayName(self) -> str:
        """Returns the display name for this tool, as shown in the tool menu."""
        ...

    @abstractmethod
    def icon(self) -> QIcon:
        """Returns the icon for this tool."""
        ...

    def setParentWidget(self, parent: QWidget) -> None:
        """Set the parent widget for this tool."""
        raise NotImplementedError("setParentWidget must be implemented by subclass")

    @abstractmethod
    def tooltip(self) -> str:
        """Returns the tooltip for this tool."""
        ...


# Forward declarations for interfaces that reference each other
class IOrganizer(ABC):
    """Interface to class that provides information about the running session."""

    @abstractmethod
    def appVersion(self) -> VersionInfo:
        """Returns the running version of Mod Organizer."""
        ...

    @abstractmethod
    def basePath(self) -> str:
        """Returns the absolute path to the base directory of Mod Organizer."""
        ...

    @abstractmethod
    def createMod(self, name: GuessedString) -> IModInterface | None:
        """Create a new mod with the specified name."""
        ...

    @abstractmethod
    def createNexusBridge(self) -> IModRepositoryBridge:
        """Create a new Nexus interface."""
        ...

    @abstractmethod
    def downloadManager(self) -> IDownloadManager:
        """Returns the interface to the download manager."""
        ...

    @abstractmethod
    def downloadsPath(self) -> str:
        """Returns the absolute path to the download directory."""
        ...

    @abstractmethod
    def gameFeatures(self) -> IGameFeatures:
        """Returns the interface to the game features."""
        ...

    @abstractmethod
    def managedGame(self) -> IPluginGame | None:
        """Returns the plugin corresponding to the current game."""
        ...

    @staticmethod
    def getPluginDataPath() -> str:
        """Returns the directory for plugin data."""
        raise NotImplementedError("getPluginDataPath must be implemented")

    @abstractmethod
    def isPluginEnabled(self, plugin: str | IPlugin) -> bool:
        """Check if a plugin is enabled."""
        ...

    @abstractmethod
    def modList(self) -> IModList:
        """Returns the interface to the mod list."""
        ...

    @abstractmethod
    def modsPath(self) -> str:
        """Returns the (absolute) path to the mods directory."""
        ...

    @abstractmethod
    def pluginList(self) -> IPluginList:
        """Returns the plugin list interface."""
        ...

    @abstractmethod
    def pluginSetting(self, plugin_name: str, key: str) -> MoVariant:
        """Retrieve settings of plugins."""
        ...

    @abstractmethod
    def profile(self) -> IProfile:
        """Returns the interface to the current profile."""
        ...

    @abstractmethod
    def profileName(self) -> str:
        """Returns the name of the current profile."""
        ...

    @abstractmethod
    def profilePath(self) -> str:
        """Returns the absolute path to the active profile."""
        ...

    @abstractmethod
    def refresh(self, save_changes: bool = True) -> None:
        """Refresh the internal mods file structure from disk."""
        ...

    @abstractmethod
    def setPluginSetting(self, plugin_name: str, key: str, value: MoVariant) -> None:
        """Set the specified setting for a plugin."""
        ...


class IModInterface(ABC):
    """Interface to a mod."""

    @abstractmethod
    def absolutePath(self) -> str:
        """Returns absolute path to the mod to be used in file system operations."""
        ...

    @abstractmethod
    def name(self) -> str:
        """Returns the name of this mod."""
        ...

    @abstractmethod
    def version(self) -> VersionInfo:
        """Returns the current version of this mod."""
        ...


class IModList(ABC):
    """Interface to the mod-list."""

    @abstractmethod
    def allMods(self) -> Sequence[str]:
        """Returns a list containing the internal names of all installed mods."""
        ...

    @abstractmethod
    def getMod(self, name: str) -> IModInterface | None:
        """Retrieve an interface to a mod using its name."""
        ...

    @abstractmethod
    def priority(self, name: str) -> int:
        """Retrieve the priority of a mod."""
        ...


class IDownloadManager(ABC):
    """Interface to the download manager."""

    @abstractmethod
    def downloadPath(self, id: int) -> str:
        """Retrieve the (absolute) path of the specified download."""
        ...

    @abstractmethod
    def startDownloadNexusFile(self, mod_id: int, file_id: int) -> int:
        """Download a file from nexusmods.com."""
        ...

    @abstractmethod
    def startDownloadURLs(self, urls: Sequence[str]) -> int:
        """Download a file by url."""
        ...


class IModRepositoryBridge(ABC):
    """Interface to mod repository (e.g., Nexus Mods)."""

    @abstractmethod
    def requestDescription(
        self, game_name: str, mod_id: int, user_data: MoVariant
    ) -> None:
        """Request description of a mod."""
        ...

    @abstractmethod
    def requestDownloadURL(
        self, game_name: str, mod_id: int, file_id: int, user_data: MoVariant
    ) -> None:
        """Request download URL for mod file."""
        ...

    @abstractmethod
    def requestFiles(self, game_name: str, mod_id: int, user_data: MoVariant) -> None:
        """Request the list of files belonging to a mod."""
        ...


class IGameFeatures(ABC):
    """Interface for the game features."""

    @abstractmethod
    def gameFeature(
        self, feature_type: Type[GameFeatureType]
    ) -> GameFeatureType | None:
        """Retrieve the given game feature, if one exists."""
        ...

    @abstractmethod
    def registerFeature(
        self,
        games: Sequence[str] | IPluginGame | GameFeature,
        feature: GameFeature,
        priority: int,
        replace: bool = False,
    ) -> bool:
        """Register game feature for all games."""
        ...

    @abstractmethod
    def unregisterFeature(self, feature: GameFeature) -> bool:
        """Unregister the given game feature."""
        ...


class IPluginList(ABC):
    """Primary interface to the list of plugins."""

    @abstractmethod
    def pluginNames(self) -> Sequence[str]:
        """Returns the list of all plugin names."""
        ...

    @abstractmethod
    def priority(self, name: str) -> int:
        """Retrieve the priority of a plugin."""
        ...

    @abstractmethod
    def state(self, name: str) -> PluginState:
        """Retrieve the state of a plugin."""
        ...


class IProfile(ABC):
    """Interface to interact with Mod Organizer 2 profiles."""

    @abstractmethod
    def absolutePath(self) -> str:
        """Returns the absolute path to the profile folder."""
        ...

    @abstractmethod
    def name(self) -> str:
        """Returns the name of this profile."""
        ...


class IPluginGame(IPlugin):
    """Base classes for game plugins."""

    @abstractmethod
    def binaryName(self) -> str:
        """Returns the name of the default executable to run."""
        ...

    @abstractmethod
    def dataDirectory(self) -> QDir:
        """Returns the path to the directory containing data."""
        ...

    @abstractmethod
    def detectGame(self) -> None:
        """Detect the game."""
        ...

    @abstractmethod
    def gameDirectory(self) -> QDir:
        """Returns the directory containing the game installation."""
        ...

    @abstractmethod
    def gameIcon(self) -> QIcon:
        """Returns the icon representing the game."""
        ...

    @abstractmethod
    def gameName(self) -> str:
        """Returns the name of the game (for internal usage)."""
        ...

    @abstractmethod
    def gameShortName(self) -> str:
        """Returns the short name of the game."""
        ...

    @abstractmethod
    def gameVersion(self) -> str:
        """Returns the version of the game."""
        ...

    @abstractmethod
    def getLauncherName(self) -> str:
        """Returns the name of the launcher executable to run."""
        ...

    @abstractmethod
    def getSupportURL(self) -> str:
        """Returns an URL for the support page of this game."""
        ...

    @abstractmethod
    def initializeProfile(self, directory: QDir, settings: ProfileSetting) -> None:
        """Initialize a profile for this game."""
        ...

    @abstractmethod
    def isInstalled(self) -> bool:
        """Returns True if this game has been discovered as installed."""
        ...

    @abstractmethod
    def listSaves(self, folder: QDir) -> list[ISaveGame]:
        """List saves in the given directory."""
        ...

    @abstractmethod
    def looksValid(self, directory: QDir) -> bool:
        """Check if the given directory looks like a valid game installation."""
        ...

    @abstractmethod
    def nexusGameID(self) -> int:
        """Retrieve the Nexus game ID for this game."""
        ...

    @abstractmethod
    def savesDirectory(self) -> QDir:
        """Returns the directory where save games are stored."""
        ...

    @abstractmethod
    def setGamePath(self, path: str) -> None:
        """Set the path to the managed game."""
        ...

    @abstractmethod
    def validShortNames(self) -> Sequence[str]:
        """Retrieve the valid 'short' names for this game."""
        ...


class IInstallationManager(ABC):
    """Interface to the installation manager."""

    @abstractmethod
    def getSupportedExtensions(self) -> Sequence[str]:
        """Returns the extensions of archives supported by this installation manager."""
        ...

    @abstractmethod
    def installArchive(
        self,
        mod_name: GuessedString,
        archive: str | os.PathLike | QFileInfo,
        mod_id: int = 0,
    ) -> tuple[InstallResult, str, int]:
        """Install the given archive."""
        ...


# Standalone functions
def getFileVersion(filepath: str | os.PathLike | QFileInfo) -> str:
    """Retrieve the file version of the given executable."""
    return ""


def getIconForExecutable(executable: str | os.PathLike | QFileInfo) -> QIcon:
    """Retrieve the icon of an executable."""
    return QIcon()


def getProductVersion(executable: str | os.PathLike | QFileInfo) -> str:
    """Retrieve the product version of the given executable."""
    return ""


# Type alias for API compatibility with original mobase module
Mapping = FileMapping
