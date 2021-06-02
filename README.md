# Codeforces API


An unofficial Codeforces API to fetch contest and problem details. Built using [FastAPI](https://github.com/tiangolo/fastapi). Hosted using [Deta](https://www.deta.sh/) at https://4y2rzj.deta.dev/




### Response Schema
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
View the [OpenAPI Specification](https://4y2rzj.deta.dev/openapi.json)

View [Documentation](https://4y2rzj.deta.dev/docs)
