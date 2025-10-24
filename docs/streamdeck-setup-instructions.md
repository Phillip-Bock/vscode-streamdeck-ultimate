# Stream Deck Setup Instructions for VS Code

## Prerequisites
1. Stream Deck hardware (3x5 button layout)
2. Stream Deck software installed
3. VS Code with Stream Deck extension installed
4. Extension: 'Stream Deck for Visual Studio Code' by Nicollas R.

## Installation Steps

### 1. Install VS Code Extension
```bash
# In VS Code, press Ctrl+P and paste:
ext install nicollasr.vscode-streamdeck
```

### 2. Configure Stream Deck Plugin
1. Open Stream Deck software
2. Find 'Visual Studio Code' in the plugin list
3. Drag 'Visual Studio Code: Execute Command' action to desired button
4. Configure each button with the commands listed in the guide

### 3. Getting Command IDs
To add custom commands:
1. In VS Code: File → Preferences → Keyboard Shortcuts
2. Find your desired command
3. Right-click → 'Copy Command ID'
4. Paste this ID into Stream Deck button configuration

### 4. Organize Your Pages
Stream Deck software allows multiple pages:
- Create a new page for each category (Navigation, Editing, Terminal, etc.)
- Use the page navigation buttons to switch between pages
- Consider adding a 'home' button on each page to return to your main page

## Configuration Method
