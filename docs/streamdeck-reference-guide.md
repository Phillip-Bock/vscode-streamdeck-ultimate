# Stream Deck VS Code Configuration Guide

## Quick Reference for All Pages

### Page: Navigation & Files

| Position | Title | Command | Description |
|----------|-------|---------|-------------|
| Row 1, Col 1 | Quick Open | `workbench.action.quickOpen` | Open file quickly (Ctrl+P) |
| Row 1, Col 2 | Command Palette | `workbench.action.showCommands` | Open command palette (Ctrl+Shift+P) |
| Row 1, Col 3 | Go to Symbol | `workbench.action.gotoSymbol` | Navigate to symbol in file (Ctrl+Shift+O) |
| Row 1, Col 4 | Go to Line | `workbench.action.gotoLine` | Go to specific line (Ctrl+G) |
| Row 1, Col 5 | File Explorer | `workbench.view.explorer` | Toggle file explorer |
| Row 2, Col 1 | Search | `workbench.view.search` | Open search panel |
| Row 2, Col 2 | Source Control | `workbench.view.scm` | Open source control |
| Row 2, Col 3 | Extensions | `workbench.view.extensions` | Open extensions panel |
| Row 2, Col 4 | Close Editor | `workbench.action.closeActiveEditor` | Close current file |
| Row 2, Col 5 | Close All | `workbench.action.closeAllEditors` | Close all open files |
| Row 3, Col 1 | Split Editor | `workbench.action.splitEditor` | Split editor view |
| Row 3, Col 2 | Next Editor | `workbench.action.nextEditor` | Go to next tab |
| Row 3, Col 3 | Prev Editor | `workbench.action.previousEditor` | Go to previous tab |
| Row 3, Col 4 | New File | `workbench.action.files.newUntitledFile` | Create new file |
| Row 3, Col 5 | Save All | `workbench.action.files.saveAll` | Save all open files |

### Page: Code Editing

| Position | Title | Command | Description |
|----------|-------|---------|-------------|
| Row 1, Col 1 | Format Doc | `editor.action.formatDocument` | Format entire document |
| Row 1, Col 2 | Format Select | `editor.action.formatSelection` | Format selected code |
| Row 1, Col 3 | Comment Line | `editor.action.commentLine` | Toggle line comment |
| Row 1, Col 4 | Block Comment | `editor.action.blockComment` | Toggle block comment |
| Row 1, Col 5 | Rename Symbol | `editor.action.rename` | Rename symbol (F2) |
| Row 2, Col 1 | Find | `actions.find` | Find in file |
| Row 2, Col 2 | Replace | `editor.action.startFindReplaceAction` | Find and replace |
| Row 2, Col 3 | Go to Definition | `editor.action.revealDefinition` | Jump to definition |
| Row 2, Col 4 | Peek Definition | `editor.action.peekDefinition` | Peek at definition |
| Row 2, Col 5 | Find References | `editor.action.goToReferences` | Find all references |
| Row 3, Col 1 | Move Line Up | `editor.action.moveLinesUpAction` | Move line up |
| Row 3, Col 2 | Move Line Down | `editor.action.moveLinesDownAction` | Move line down |
| Row 3, Col 3 | Copy Line Up | `editor.action.copyLinesUpAction` | Duplicate line up |
| Row 3, Col 4 | Copy Line Down | `editor.action.copyLinesDownAction` | Duplicate line down |
| Row 3, Col 5 | Delete Line | `editor.action.deleteLines` | Delete current line |

### Page: Terminal & Debug

| Position | Title | Command | Description |
|----------|-------|---------|-------------|
| Row 1, Col 1 | New Terminal | `workbench.action.terminal.new` | Create new terminal |
| Row 1, Col 2 | Toggle Terminal | `workbench.action.terminal.toggleTerminal` | Show/hide terminal |
| Row 1, Col 3 | Kill Terminal | `workbench.action.terminal.kill` | Close active terminal |
| Row 1, Col 4 | Clear Terminal | `workbench.action.terminal.clear` | Clear terminal output |
| Row 1, Col 5 | Split Terminal | `workbench.action.terminal.split` | Split terminal pane |
| Row 2, Col 1 | Start Debug | `workbench.action.debug.start` | Start debugging |
| Row 2, Col 2 | Stop Debug | `workbench.action.debug.stop` | Stop debugging |
| Row 2, Col 3 | Step Over | `workbench.action.debug.stepOver` | Step over function |
| Row 2, Col 4 | Step Into | `workbench.action.debug.stepInto` | Step into function |
| Row 2, Col 5 | Step Out | `workbench.action.debug.stepOut` | Step out of function |
| Row 3, Col 1 | Toggle Breakpoint | `editor.debug.action.toggleBreakpoint` | Add/remove breakpoint |
| Row 3, Col 2 | Continue | `workbench.action.debug.continue` | Continue execution |
| Row 3, Col 3 | Restart Debug | `workbench.action.debug.restart` | Restart debugging |
| Row 3, Col 4 | Run Task | `workbench.action.tasks.runTask` | Run configured task |
| Row 3, Col 5 | Problems | `workbench.actions.view.problems` | Show problems panel |

### Page: Git Operations

| Position | Title | Command | Description |
|----------|-------|---------|-------------|
| Row 1, Col 1 | Git: Commit | `git.commit` | Commit staged changes |
| Row 1, Col 2 | Git: Push | `git.push` | Push to remote |
| Row 1, Col 3 | Git: Pull | `git.pull` | Pull from remote |
| Row 1, Col 4 | Git: Sync | `git.sync` | Sync with remote |
| Row 1, Col 5 | Git: Fetch | `git.fetch` | Fetch from remote |
| Row 2, Col 1 | Stage All | `git.stageAll` | Stage all changes |
| Row 2, Col 2 | Unstage All | `git.unstageAll` | Unstage all changes |
| Row 2, Col 3 | Show Changes | `git.openChange` | View file changes |
| Row 2, Col 4 | New Branch | `git.branch` | Create new branch |
| Row 2, Col 5 | Checkout | `git.checkout` | Switch branch |
| Row 3, Col 1 | View History | `git.viewHistory` | View commit history |
| Row 3, Col 2 | Stash | `git.stash` | Stash changes |
| Row 3, Col 3 | Pop Stash | `git.stashPop` | Apply stashed changes |
| Row 3, Col 4 | Merge | `git.merge` | Merge branch |
| Row 3, Col 5 | Clone Repo | `git.clone` | Clone repository |

### Page: Workspace & Views

| Position | Title | Command | Description |
|----------|-------|---------|-------------|
| Row 1, Col 1 | Zen Mode | `workbench.action.toggleZenMode` | Toggle zen mode |
| Row 1, Col 2 | Fullscreen | `workbench.action.toggleFullScreen` | Toggle fullscreen |
| Row 1, Col 3 | Toggle Sidebar | `workbench.action.toggleSidebarVisibility` | Show/hide sidebar |
| Row 1, Col 4 | Toggle Panel | `workbench.action.togglePanel` | Show/hide bottom panel |
| Row 1, Col 5 | Settings | `workbench.action.openSettings` | Open settings |
| Row 2, Col 1 | Open Folder | `workbench.action.files.openFolder` | Open folder/workspace |
| Row 2, Col 2 | Close Folder | `workbench.action.closeFolder` | Close current workspace |
| Row 2, Col 3 | Recent Workspaces | `workbench.action.openRecent` | Open recent workspaces |
| Row 2, Col 4 | New Window | `workbench.action.newWindow` | Open new VS Code window |
| Row 2, Col 5 | Reload Window | `workbench.action.reloadWindow` | Reload VS Code |
| Row 3, Col 1 | Zoom In | `workbench.action.zoomIn` | Increase zoom level |
| Row 3, Col 2 | Zoom Out | `workbench.action.zoomOut` | Decrease zoom level |
| Row 3, Col 3 | Reset Zoom | `workbench.action.zoomReset` | Reset zoom to default |
| Row 3, Col 4 | Keybindings | `workbench.action.openGlobalKeybindings` | Edit keyboard shortcuts |
| Row 3, Col 5 | Color Theme | `workbench.action.selectTheme` | Change color theme |

### Page: Advanced Features

| Position | Title | Command | Description |
|----------|-------|---------|-------------|
| Row 1, Col 1 | Multi-Cursor | `editor.action.insertCursorAbove` | Add cursor above |
| Row 1, Col 2 | Select All Occurrences | `editor.action.selectHighlights` | Select all matching text |
| Row 1, Col 3 | Expand Selection | `editor.action.smartSelect.expand` | Smart expand selection |
| Row 1, Col 4 | Shrink Selection | `editor.action.smartSelect.shrink` | Smart shrink selection |
| Row 1, Col 5 | Transform to Upper | `editor.action.transformToUppercase` | Convert to uppercase |
| Row 2, Col 1 | Transform to Lower | `editor.action.transformToLowercase` | Convert to lowercase |
| Row 2, Col 2 | Sort Lines Asc | `editor.action.sortLinesAscending` | Sort lines A-Z |
| Row 2, Col 3 | Sort Lines Desc | `editor.action.sortLinesDescending` | Sort lines Z-A |
| Row 2, Col 4 | Trim Trailing Space | `editor.action.trimTrailingWhitespace` | Remove trailing whitespace |
| Row 2, Col 5 | Join Lines | `editor.action.joinLines` | Join selected lines |
| Row 3, Col 1 | Fold All | `editor.foldAll` | Collapse all code blocks |
| Row 3, Col 2 | Unfold All | `editor.unfoldAll` | Expand all code blocks |
| Row 3, Col 3 | Toggle Fold | `editor.toggleFold` | Toggle current fold |
| Row 3, Col 4 | Show Snippets | `editor.action.insertSnippet` | Insert snippet |
| Row 3, Col 5 | Emmet Expand | `editor.emmet.action.expandAbbreviation` | Expand Emmet abbreviation |
