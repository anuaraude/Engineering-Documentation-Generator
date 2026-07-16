<p align="center">
  <img src="assets/images/banner.png" alt="Engineering Documentation Generator Banner">
</p>

# Engineering Documentation Generator

> A modular command-line tool for assembling standardized engineering documents from reusable Markdown section templates.

---

## About

Engineering projects often require documentation before implementation can begin.

Although every project has different objectives, many documentation tasks follow recurring structures. Rewriting these sections manually consumes time and can produce inconsistent results.

The Engineering Documentation Generator addresses this problem by collecting project information and assembling documents from independent Markdown section templates.

The objective is not to replace engineering judgment, but to automate repetitive formatting and documentation tasks while keeping the user in control of the final content.

---

## Philosophy

> Automate repetitive work, not creative thinking.

The `templates` directory acts as a reusable section library for engineering documents.

Each document type is divided into mandatory core sections and selectable optional sections. The generator requests only the information required by the chosen sections and assembles them in a standardized order.

---

## Current Capabilities

The current implementation supports:

- Command-line project and document selection.
- Collection of all mandatory README Core information.
- Modular Markdown section templates.
- Placeholder replacement using project configuration data.
- Assembly of six independent Core templates into one README preview.
- Separation of interface, configuration, template loading, and document generation responsibilities.

---

## Current README Sections

### Implemented

- Header
- About
- Getting Started
- Project Status
- Author
- License

### Planned Optional Sections

- Features
- Project Structure
- Examples
- Documentation
- Roadmap
- Contributing

Additional specialized sections will be considered in later versions.

---

## Project Structure

```text
Engineering-Documentation-Generator/
├── assets/
├── docs/
├── src/
├── templates/
│   ├── readme/
│   │   ├── core/
│   │   │   ├── header.md
│   │   │   ├── about.md
│   │   │   ├── getting_started.md
│   │   │   ├── project_status.md
│   │   │   ├── author.md
│   │   │   └── license.md
│   │   └── optional/
│   └── technical_knowledge_document/
├── tests/
├── LICENSE
├── README.md
└── requirements.txt
```

## Documentation

- [Project Requirements](docs/project-requirements.md)
- [Architecture Design](docs/architecture-design.md)
- [README Standard](docs/readme-standard.md)

## Project Status

🚧 **Version 0.4 — README Core completed**

The generator now assembles all six mandatory README Core sections from independent Markdown templates.

Optional section selection, interactive review, and file output remain under development.

## License

This project is distributed under the terms defined in the [LICENSE](LICENSE) file.

*"Good software begins with good engineering."*