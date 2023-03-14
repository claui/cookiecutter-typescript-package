import { hello } from "{{ cookiecutter.project_slug }}";

test("prints Hello, world!", () => {
  expect(hello()).toEqual("Hello, world!");
});
