# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-24

### Added
- Initial release of Stream Deck VS Code Ultimate Configuration
- 90 professionally curated VS Code commands across 6 themed pages
- Page 1: Navigation & Files (15 commands)
- Page 2: Code Editing (15 commands)
- Page 3: Terminal & Debug (15 commands)
- Page 4: Git Operations (15 commands)
- Page 5: Workspace & Views (15 commands)
- Page 6: Advanced Features (15 commands)
- Comprehensive documentation package
  - START-HERE.txt quick start guide
  - Step-by-step setup instructions
  - Complete command reference
  - Individual page configuration guides
- Beautiful HTML cheat sheet for printing/reference
- Python scripts for configuration generation
- JSON configuration files for customization
- CSV export for importing
- GitHub issue templates (Bug Report, Feature Request, Questions, Custom Config Sharing)
- GitHub Actions workflow for configuration validation
- Pull request template
- Contributing guidelines
- Code of Conduct
- Security policy
- MIT License

### Documentation
- Complete setup guide with troubleshooting
- Visual layout diagrams
- Command ID reference
- Customization instructions
- File organization guide

### Tools
- `generate_streamdeck_config.py` - Regenerate all documentation
- `quick_configurator.py` - Additional configuration utilities

## [Unreleased]

### Planned Features
- Support for Stream Deck XL (8×4 layout)
- Support for Stream Deck Mini (2×3 layout)
- Language-specific command pages (Python, JavaScript, TypeScript, etc.)
- Custom icon pack
- Video tutorials
- Community-contributed configurations
- Integration with popular VS Code extensions
- Automated Stream Deck profile export

---

## How to Update

### For Users
When a new version is released:
1. Pull the latest changes: `git pull origin main`
2. Review the changelog to see what's new
3. Regenerate documentation if config changed: `python3 scripts/generate_streamdeck_config.py`
4. Update your Stream Deck buttons as needed

### For Contributors
When contributing:
1. Update this CHANGELOG.md with your changes
2. Follow the format: Added/Changed/Deprecated/Removed/Fixed/Security
3. Add entry under `[Unreleased]` section
4. Link to relevant issues/PRs

---

## Version History

- **[1.0.0]** - Initial release (2025-10-24)

---

*For a detailed list of changes, see the [commit history](https://github.com/Phillip-Bock/vscode-streamdeck-ultimate/commits/main).*
