# GitHub Templates & Automation

This folder contains issue templates, pull request templates, and GitHub Actions workflows for the repository.

## 📁 Contents

### Issue Templates (`ISSUE_TEMPLATE/`)

- **bug_report.md** - Template for reporting bugs
- **feature_request.md** - Template for suggesting new features
- **question.md** - Template for asking questions
- **share_config.md** - Template for sharing custom configurations
- **config.yml** - Configuration for issue templates

### Pull Request Template

- **PULL_REQUEST_TEMPLATE.md** - Template for all pull requests

### GitHub Actions (`workflows/`)

- **validate.yml** - Automated validation of configuration files

## 🎯 Purpose

These templates help maintain consistent, high-quality issues and pull requests by:

- Ensuring bug reports include all necessary information
- Guiding feature requests with structured format
- Encouraging users to check documentation first
- Making it easy to share custom configurations
- Automating code quality checks

## 🚀 How They Work

### Issue Templates

When someone clicks "New Issue" on GitHub, they'll see 4 template options:

1. **🐛 Bug Report** - Auto-labeled as `bug`
2. **💡 Feature Request** - Auto-labeled as `enhancement`
3. **❓ Question or Help** - Auto-labeled as `question`
4. **🎨 Share Custom Configuration** - Auto-labeled as `custom-config`

Each template includes:
- Clear sections for required information
- Helpful placeholders and examples
- Checklists to ensure quality
- Automatic labels

### Pull Request Template

When someone creates a PR, they'll see:
- Description section
- Type of change checkboxes
- Testing checklist
- Screenshots section
- Self-review checklist

### GitHub Actions Workflow

The `validate.yml` workflow runs automatically on:
- Every push to `main` branch
- Every pull request

It validates:
- JSON configuration files are valid
- All required files exist
- Python scripts execute without errors

## 🔧 Customization

Feel free to customize these templates by editing the markdown files. The YAML front matter controls:

```yaml
---
name: Template Name          # Name shown in GitHub UI
about: Description           # Description shown in GitHub UI
title: '[PREFIX] '          # Auto-populated issue title
labels: label-name          # Auto-applied labels
assignees: ''               # Auto-assigned users (leave empty)
---
```

## 📊 Labels Used

Make sure these labels exist in your repository:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `question` - Further information requested
- `custom-config` - Community shared configuration
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed

## 🔗 Resources

- [GitHub Issue Templates Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Pull Request Template Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)

## 💡 Tips

- Review and respond to issues within 24-48 hours
- Use labels to organize issues
- Close stale issues after 30 days of inactivity
- Thank contributors for their submissions
- Keep the templates updated as needs evolve
