# 🎛️ Stream Deck VS Code Configuration Package
**Your Complete Setup for 90 VS Code Commands Across 6 Pages**

---

## 📦 What You've Got

This package includes **everything** you need to configure your Stream Deck (3x5 layout) with powerful VS Code commands organized across 6 themed pages:

### 🎯 The 6 Pages:
1. **Navigation & Files** - Opening files, switching tabs, file explorer
2. **Code Editing** - Formatting, commenting, refactoring, find/replace
3. **Terminal & Debug** - Terminal management, debugging controls
4. **Git Operations** - Commit, push, pull, branches, stash
5. **Workspace & Views** - Zen mode, fullscreen, zoom, themes
6. **Advanced Features** - Multi-cursor, text transforms, folding, snippets

### 📁 Files Included:

#### 🚀 Quick Start Files (Start Here!)
- **`streamdeck-setup-step-by-step.txt`** - Page-by-page setup instructions (EASIEST)
- **`streamdeck-cheatsheet.html`** - Beautiful visual reference (open in browser & print!)
- **`streamdeck-profile-guide.txt`** - Complete overview of all buttons

#### 📋 Individual Page Guides
- `page-navigation-and-files.txt`
- `page-code-editing.txt`
- `page-terminal-and-debug.txt`
- `page-git-operations.txt`
- `page-workspace-and-views.txt`
- `page-advanced-features.txt`

#### 📊 Reference & Import Files
- **`streamdeck-config-generator.json`** - Master configuration file
- **`streamdeck-import.csv`** - CSV for importing (if supported by tools)
- **`streamdeck-reference-guide.md`** - Markdown reference
- **`streamdeck-commands-list.md`** - All commands in one list
- **`streamdeck-visual-layout.md`** - ASCII art layouts

#### 🔧 Customization Tools
- **`streamdeck-custom-template.json`** - Template for creating your own page
- **`generate_streamdeck_config.py`** - Python script to regenerate configs
- **`quick_configurator.py`** - Python script for additional utilities

---

## 🚀 Quick Start Guide

### Step 1: Prerequisites
✅ Stream Deck hardware (3 rows × 5 columns layout)  
✅ Stream Deck software installed  
✅ VS Code installed  
✅ VS Code Stream Deck extension

### Step 2: Install VS Code Extension
1. Open VS Code
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Paste: `ext install nicollasr.vscode-streamdeck`
4. Press Enter

**OR** search for "Stream Deck for Visual Studio Code" by Nicollas R. in the Extensions marketplace.

### Step 3: Configure Your Stream Deck

**EASIEST METHOD:** Follow the step-by-step guide:
- Open `streamdeck-setup-step-by-step.txt`
- Follow instructions page by page
- Each button tells you exactly what to do

**VISUAL METHOD:** Print the cheat sheet:
- Open `streamdeck-cheatsheet.html` in your browser
- Click the "Print Cheat Sheet" button (or press `Ctrl+P`)
- Keep it next to your desk as reference

### Step 4: Configure Each Button
For each button on your Stream Deck:

1. **Open Stream Deck Software**
2. **Drag** "Visual Studio Code: Execute Command" action to button position
3. **Enter the Command ID** (from the guide files)
4. **Set the Title** (suggested titles in guides)
5. **Optional:** Add an icon/emoji (suggested in guides)

---

## 📖 How to Use This Package

### For First-Time Setup:
1. Start with `streamdeck-setup-step-by-step.txt`
2. Have `streamdeck-cheatsheet.html` open in browser for reference
3. Configure one page at a time
4. Test buttons as you go

### For Quick Reference:
- Open `streamdeck-cheatsheet.html` and bookmark it
- Print it and keep near your Stream Deck
- Use page navigation buttons to switch between views

### For Finding Specific Commands:
- Check `streamdeck-commands-list.md` for alphabetical listing
- Check `streamdeck-reference-guide.md` for organized tables
- Use individual `page-*.txt` files for specific categories

### For Customization:
- Copy `streamdeck-custom-template.json`
- Modify the command IDs to your preferred commands
- Use Python scripts to regenerate documentation

---

## 🎨 Getting Command IDs for Custom Buttons

Want to add your own commands? Here's how:

1. Open VS Code
2. Go to **File → Preferences → Keyboard Shortcuts** (or press `Ctrl+K Ctrl+S`)
3. Search for the command you want
4. **Right-click** on the command
5. Select **"Copy Command ID"**
6. Paste this ID into your Stream Deck button configuration

Example Command IDs:
- `workbench.action.quickOpen` - Quick Open File
- `editor.action.formatDocument` - Format Document
- `workbench.action.terminal.new` - New Terminal

---

## 💡 Pro Tips

### Organize Your Pages
- Keep most-used commands on Page 1
- Group related commands together
- Use page navigation buttons to switch quickly

### Visual Consistency
- Use consistent emojis/icons for similar actions
- Color-code by category (if your Stream Deck supports it)
- Keep button titles short and clear

### Testing
- Test each button after configuration
- Make sure VS Code window is focused when pressing buttons
- Check the VS Code status bar for connection status

### Workflow Optimization
Start with these essential pages:
1. **Navigation & Files** - Daily basics
2. **Code Editing** - Your main work
3. **Terminal & Debug** - Development workflow

Then add specialized pages as needed:
4. **Git Operations** - For version control heavy work
5. **Workspace & Views** - For presentation/focus modes
6. **Advanced Features** - For power users

---

## 🔧 Troubleshooting

### Button Not Working?
- ✅ Check VS Code window is focused
- ✅ Verify command ID is correct (no typos)
- ✅ Check extension is installed and active (status bar)
- ✅ Try reloading VS Code window

### Extension Not Connecting?
- ✅ Check firewall settings (port 9667)
- ✅ Try using 127.0.0.1 instead of localhost
- ✅ Restart both Stream Deck software and VS Code
- ✅ Check extension settings in VS Code

### Command ID Not Found?
- ✅ Some commands may be from extensions - install required extension
- ✅ Double-check spelling of command ID
- ✅ Look up command in Keyboard Shortcuts panel

---

## 📚 Complete Command List Summary

### Page 1: Navigation & Files (15 buttons)
Quick Open, Command Palette, Go to Symbol, Go to Line, File Explorer, Search, Source Control, Extensions, Close Editor, Close All, Split Editor, Next/Previous Editor, New File, Save All

### Page 2: Code Editing (15 buttons)
Format Document/Selection, Comment Line/Block, Rename Symbol, Find, Replace, Go to/Peek Definition, Find References, Move/Copy Line Up/Down, Delete Line

### Page 3: Terminal & Debug (15 buttons)
New/Toggle/Kill/Clear Terminal, Split Terminal, Start/Stop Debug, Step Over/Into/Out, Toggle Breakpoint, Continue, Restart, Run Task, Problems

### Page 4: Git Operations (15 buttons)
Commit, Push, Pull, Sync, Fetch, Stage/Unstage All, Show Changes, New Branch, Checkout, View History, Stash, Pop Stash, Merge, Clone

### Page 5: Workspace & Views (15 buttons)
Zen Mode, Fullscreen, Toggle Sidebar/Panel, Settings, Open/Close Folder, Recent Workspaces, New/Reload Window, Zoom In/Out/Reset, Keybindings, Color Theme

### Page 6: Advanced Features (15 buttons)
Multi-Cursor, Select All Occurrences, Expand/Shrink Selection, Transform Upper/Lower, Sort Lines, Trim Whitespace, Join Lines, Fold/Unfold All, Toggle Fold, Snippets, Emmet

**Total: 90 programmable buttons!**

---

## 🎁 Bonus Features

### HTML Cheat Sheet
The `streamdeck-cheatsheet.html` file is interactive:
- Responsive design works on any screen
- Printable (click Print button or Ctrl+P)
- Hover effects show you which button you're looking at
- Color-coded by page type

### Python Scripts
If you want to modify or extend the configuration:

```bash
# Regenerate all documentation files
python3 generate_streamdeck_config.py

# Create custom configurations
python3 quick_configurator.py
```

---

## 📝 Customization Example

Want to add your own page? Edit `streamdeck-custom-template.json`:

```json
{
  "page_custom": {
    "name": "My Custom Page",
    "buttons": [
      {
        "position": [0, 0],
        "title": "My Command",
        "command": "your.command.id",
        "icon": "💡",
        "description": "Does something awesome"
      }
    ]
  }
}
```

Then run: `python3 generate_streamdeck_config.py` to create updated docs!

---

## 🌟 What Makes This Configuration Great?

✅ **Complete Coverage** - 90 commands across all major VS Code features  
✅ **Organized** - Logically grouped into 6 themed pages  
✅ **Well-Documented** - Multiple formats for every learning style  
✅ **Beginner-Friendly** - Step-by-step instructions  
✅ **Professional** - Carefully selected, most-useful commands  
✅ **Printable** - Beautiful cheat sheet for desk reference  
✅ **Customizable** - Easy to modify and extend  
✅ **Tested** - All commands verified to work in VS Code

---

## 📞 Need Help?

### Documentation
- VS Code Keyboard Shortcuts: `Ctrl+K Ctrl+S`
- Extension Docs: https://marketplace.visualstudio.com/items?itemName=nicollasr.vscode-streamdeck
- VS Code Keybindings: https://code.visualstudio.com/docs/getstarted/keybindings

### Common Resources
- All command IDs are standard VS Code commands
- Some Git commands require Git extension (built-in)
- Debug commands work with any configured debugger

---

## 🎉 You're Ready!

Your Stream Deck is about to become a **VS Code powerhouse**! 

**Recommended first steps:**
1. ✅ Open `streamdeck-cheatsheet.html` in your browser
2. ✅ Print it for reference
3. ✅ Follow `streamdeck-setup-step-by-step.txt` 
4. ✅ Configure Page 1 (Navigation) first
5. ✅ Test all buttons
6. ✅ Continue with remaining pages

**Happy coding!** 🚀

---

*Created with ❤️ for efficient VS Code development*  
*Version 1.0 - Optimized for Stream Deck 3x5 layout*
