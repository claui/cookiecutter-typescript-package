# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_description }}

## What it does

(tbd)

## How to install

Using the npm CLI:

```shell
npm install {{ cookiecutter.project_slug }}
```

Using Yarn:

```shell
yarn add {{ cookiecutter.project_slug }}
```

## License

{% if cookiecutter.project_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.project_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
