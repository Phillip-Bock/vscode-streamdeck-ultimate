# Contributing to Stream Deck VS Code Configuration

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 Ways to Contribute

- 🐛 Report bugs or issues
- 💡 Suggest new commands or improvements
- 📝 Improve documentation
- 🔧 Add support for different Stream Deck layouts
- 🌍 Create language-specific configurations
- ✨ Share your custom page configurations

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/streamdeck-vscode-config.git
   ```
3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Contribution Guidelines

### Adding New Commands

If you want to add new VS Code commands:

1. Verify the command ID works in VS Code
2. Add it to `streamdeck-config-generator.json`
3. Run the regeneration script:
   ```bash
   python3 generate_streamdeck_config.py
   ```
4. Test the generated documentation
5. Submit a pull request

### Documentation Improvements

- Keep instructions clear and beginner-friendly
- Include examples when possible
- Maintain consistent formatting
- Test instructions on a fresh setup

### Code Style

For Python scripts:
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Include comments for complex logic
- Test scripts before submitting

## 🔍 Pull Request Process

1. **Update documentation** - If your changes affect how users configure their Stream Deck
2. **Test thoroughly** - Ensure all generated files are correct
3. **Describe your changes** - Write a clear PR description
4. **Link related issues** - Reference any related issue numbers

### Pull Request Template

```markdown
## Description
[Describe what this PR does]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Configuration improvement

## Testing
- [ ] Tested command IDs in VS Code
- [ ] Regenerated documentation
- [ ] Verified all files are correct

## Related Issues
Fixes #[issue number]
```

## 🐛 Reporting Bugs

When reporting bugs, please include:

- **Description** - Clear description of the issue
- **Steps to Reproduce** - How to reproduce the problem
- **Expected Behavior** - What should happen
- **Actual Behavior** - What actually happens
- **Environment** - OS, VS Code version, Stream Deck model
- **Screenshots** - If applicable

## 💡 Suggesting Enhancements

For feature requests or enhancements:

- **Use Case** - Explain why this would be useful
- **Proposed Solution** - How you envision it working
- **Alternatives** - Any alternative approaches you've considered
- **Additional Context** - Screenshots, examples, etc.

## 🎨 Custom Configurations

If you've created a great custom configuration:

1. Create a folder in `custom-configs/`
2. Include your modified JSON file
3. Add a README explaining your changes
4. Share what use case it solves

Example structure:
```
custom-configs/
└── python-developer/
    ├── README.md
    ├── python-streamdeck-config.json
    └── screenshot.png
```

## 📋 Command Selection Criteria

When proposing new commands, consider:

- **Frequency of Use** - Is this commonly used?
- **Keyboard Alternative** - Is it hard to trigger with keyboard?
- **Workflow Benefit** - Does it improve workflow significantly?
- **VS Code Version** - Is it available in recent VS Code versions?
- **Conflicts** - Does it conflict with existing commands?

## 🔄 Regenerating Documentation

After modifying `streamdeck-config-generator.json`:

```bash
# Regenerate all documentation files
python3 generate_streamdeck_config.py

# Review changes
git status
git diff
```

## ✅ Code Review Process

All submissions require review. We look for:

- Functionality - Does it work as intended?
- Documentation - Is it well documented?
- Code Quality - Is the code clean and maintainable?
- Testing - Has it been tested?
- Style - Does it follow project conventions?

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in the project README. Thank you for making this project better!

## 💬 Questions?

- Open a GitHub Discussion
- Comment on an existing issue
- Reach out to maintainers

---

**Thank you for contributing!** 🎉
