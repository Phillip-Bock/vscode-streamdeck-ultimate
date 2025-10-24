# 🎛️ Stream Deck VS Code Configuration

> Transform your Stream Deck into a VS Code powerhouse with 90 professionally curated commands

[![VS Code](https://img.shields.io/badge/VS%20Code-Compatible-blue)](https://code.visualstudio.com/)
[![Stream Deck](https://img.shields.io/badge/Stream%20Deck-3x5%20Layout-purple)](https://www.elgato.com/stream-deck)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Commands](https://img.shields.io/badge/Commands-90-orange)](streamdeck-config-generator.json)

## ✨ Features

- 🎯 **90 VS Code Commands** - Carefully selected for maximum productivity
- 📊 **6 Themed Pages** - Logically organized workflow categories
- 📖 **Complete Documentation** - Step-by-step setup guides
- 🎨 **Beautiful Cheat Sheet** - Printable HTML reference
- 🔧 **Fully Customizable** - Python scripts and JSON templates included
- ⚡ **Bulk Configuration** - No more one-by-one button setup

## 🚀 Quick Start

### Prerequisites
- Elgato Stream Deck (3×5 button layout)
- Visual Studio Code
- [Stream Deck for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=nicollasr.vscode-streamdeck) extension

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/streamdeck-vscode-config.git
   cd streamdeck-vscode-config
   ```

2. **Install VS Code Extension**
   ```bash
   # In VS Code, press Ctrl+P and paste:
   ext install nicollasr.vscode-streamdeck
   ```

3. **Start Setup**
   - Open `START-HERE.txt` for quick start guide
   - Follow `streamdeck-setup-step-by-step.txt` for detailed instructions
   - Open `streamdeck-cheatsheet.html` in your browser as reference

## 📋 The 6 Pages

### Page 1: Navigation & Files (15 buttons)
Quick Open, Command Palette, Go to Symbol/Line, File Explorer, Search, Source Control, Extensions, Close Editor/All, Split Editor, Next/Prev Editor, New File, Save All

### Page 2: Code Editing (15 buttons)
Format Document/Selection, Comment Line/Block, Rename Symbol, Find, Replace, Go to/Peek Definition, Find References, Move/Copy Line Up/Down, Delete Line

### Page 3: Terminal & Debug (15 buttons)
New/Toggle/Kill/Clear/Split Terminal, Start/Stop/Restart Debug, Step Over/Into/Out, Continue, Toggle Breakpoint, Run Task, Problems

### Page 4: Git Operations (15 buttons)
Commit, Push, Pull, Sync, Fetch, Stage/Unstage All, Show Changes, New Branch, Checkout, View History, Stash, Pop Stash, Merge, Clone

### Page 5: Workspace & Views (15 buttons)
Zen Mode, Fullscreen, Toggle Sidebar/Panel, Settings, Open/Close Folder, Recent Workspaces, New/Reload Window, Zoom In/Out/Reset, Keybindings, Color Theme

### Page 6: Advanced Features (15 buttons)
Multi-Cursor, Select All Occurrences, Expand/Shrink Selection, Transform Upper/Lower, Sort Lines, Trim Whitespace, Join Lines, Fold/Unfold All, Toggle Fold, Snippets, Emmet

## 📁 File Structure

```
streamdeck-vscode-config/
├── START-HERE.txt                      # Quick start guide
├── README.md                           # This file
├── FILE-GUIDE.txt                      # Which file to use when
├── streamdeck-setup-step-by-step.txt   # Main setup instructions
├── streamdeck-cheatsheet.html          # Beautiful visual reference
├── streamdeck-config-generator.json    # Master configuration
├── page-*.txt                          # Individual page setup files
├── generate_streamdeck_config.py       # Regeneration script
└── quick_configurator.py               # Utility script
```

## 🎨 Visual Preview

<!-- Add screenshot of your Stream Deck or the HTML cheat sheet here -->
> 💡 **Tip:** Open `streamdeck-cheatsheet.html` in your browser to see the full visual layout!

## 🔧 Customization

### Adding Custom Commands

1. Find the command ID in VS Code:
   - `File → Preferences → Keyboard Shortcuts` (Ctrl+K Ctrl+S)
   - Right-click command → `Copy Command ID`

2. Edit `streamdeck-custom-template.json` with your commands

3. Regenerate documentation:
   ```bash
   python3 generate_streamdeck_config.py
   ```

### Modifying Existing Pages

Edit `streamdeck-config-generator.json` and run the regeneration script to update all documentation.

## 📊 Configuration Statistics

| Metric | Value |
|--------|-------|
| Total Commands | 90 |
| Total Pages | 6 |
| Buttons per Page | 15 (3×5) |
| File Formats | TXT, MD, HTML, JSON, CSV, PY |
| Setup Time | 45-120 minutes |

## 💡 Pro Tips

- **Start with Page 1** - Most essential commands for daily work
- **Print the cheat sheet** - Keep it next to your Stream Deck
- **Test as you go** - Configure a few buttons, test them, continue
- **Customize gradually** - Start with defaults, modify as needed
- **Add page navigation buttons** - Easily switch between pages

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit command suggestions
- Improve documentation
- Add support for different Stream Deck layouts
- Create language-specific configurations

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stream Deck for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=nicollasr.vscode-streamdeck) by Nicollas R.
- [Visual Studio Code](https://code.visualstudio.com/) by Microsoft
- [Elgato Stream Deck](https://www.elgato.com/stream-deck)

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/YOUR-USERNAME/streamdeck-vscode-config/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/YOUR-USERNAME/streamdeck-vscode-config/discussions)
- 📖 **VS Code Docs**: https://code.visualstudio.com/docs
- 🎛️ **Extension Docs**: https://marketplace.visualstudio.com/items?itemName=nicollasr.vscode-streamdeck

## ⭐ Star History

If this project helped you, please consider giving it a ⭐️!

---

**Made with ❤️ for VS Code developers who love efficiency**

**Version 1.0** | Optimized for Stream Deck 3×5 layout
