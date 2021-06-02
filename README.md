# Codeforces API


Built using [FastAPI](https://github.com/tiangolo/fastapi). A [Deta](https://www.deta.sh/) micro is hosted at https://4y2rzj.deta.dev/

#### contest_response:

```
{
  contest_id: integer,
  contest_name: string,
  contest_link: string,
  problems: list
  [{
    problem_id: string
    contest_id: integer
    name: string
    problem_link: string
  }],
  editorial: string,
  announcement:	string,
}
```
View the [OpenAPI specification](https://4y2rzj.deta.dev/openapi.json)
