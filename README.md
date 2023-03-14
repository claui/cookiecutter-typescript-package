# cookiecutter-typescript-package

This is the source code repository for
`cookiecutter-typescript-package`, a
[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for TypeScript packages which focuses on long-term
maintainability and a reliable setup.

## About this document

This is the **user documentation** for the Cookiecutter template.  
If you’re a **contributor**, see: [CONTRIBUTING.md](./CONTRIBUTING.md)  
For **license information,** see the bottom of this document.

## About this template

### Goals

`cookiecutter-typescript-package` is an opinionated Cookiecutter
template for TypeScript packages with a focus on:

- **long-term maintainability** of the generated project; and

- **reliability** through step-by-step instructions, enabling users
  to build, run, and work on the generated packages on diverse
  platforms.

### What you put in

The template allows you to specify:

- project slug, description, and version;

- both an author name and a copyright holder name;

- a project license (Apache 2.0 or proprietary license);

- the major Node.js version;

- your username on the NPM package registry; and

- your GitHub username where the source code repository will live.

### What you get out of it

The Cookiecutter template will give you:

- a `package.json` in the project root directory, which declares
  essential development dependencies and useful Yarn scripts;

- a `src` subdirectory, which is the root of the package source code;

- the main TypeScript module `src/index.ts`, which is the entry
  point of your package;

- linter settings for ESLint;

- `tsconfig.json` and `tsconfig.linting.json` files to configure
  the TypeScript compiler;

- a Jest setup for unit tests;

- a `.gitattributes` file;

- a `.gitignore` file;

- an `.editorconfig` file;

- a `.nvmrc` file to lock the Node.js platform version;

- a user-facing `README.md` file, which will be published alongside
  the package;

- a `CONTRIBUTING.md` file in the project root directory, aimed at
  contributors to the package;

- a `LICENSE` file; and

- settings for Visual Studio Code integration.

## Using cookiecutter-typescript-package

### System requirements

To use this Cookiecutter template, you need:

1. A system-wide Python installation.

2. Cookiecutter version 2.1 or newer.

3. The JavaScript version manager `nvm`.

4. The JavaScript package manager `yarn`.

### Checking your system-wide Python installation

Make sure you have Python 3.7 or higher installed on your system
and available in your PATH.

To check, run:

```shell
python --version
```

If that fails, try:

```shell
python3 --version
```

Proceed after you’ve confirmed one of those to work.

### Installing Cookiecutter

To install Cookiecutter, follow Cookiecutter’s [installation
instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html).

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```shell
cookiecutter gh:claui/cookiecutter-typescript-package
```

### Alternative usage

If you use `cookiecutter-typescript-package` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```shell
abbreviations:
    typescript: https://github.com/claui/cookiecutter-typescript-package.git
```

Then, to generate a project, run:

```shell
cookiecutter typescript
```

### Working on the generated package

See the generated `README.md` file.

### Contributing to this Cookiecutter template

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

Copyright (c) 2023 Claudia Pellegrino <clau@tiqua.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).

### Additional license files

This project may include additional license files other than the
Apache License. Those are part of the template, which means they may
not apply to this project. The only license that applies to this
project is the Apache License.
