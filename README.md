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
- Collection of README Header information.
- Collection of README About information.
- Modular Markdown section templates.
- Placeholder replacement using project configuration data.
- Assembly of multiple independent templates into one README preview.
- Separation of interface, configuration, template loading, and document generation responsibilities.

---

## Current README Sections

### Implemented

- Header
- About

### Planned Core Sections

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
│   │   │   └── about.md
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

🚧 Version 0.1 — Core README implementation in progress

The architecture and documentation standards have been defined.

The generator currently assembles the Header and About sections from independent Markdown templates. The remaining core sections will be implemented incrementally before optional section selection is introduced.

## License

This project is distributed under the terms defined in the [LICENSE](LICENSE) file.

*"Good software begins with good engineering."*