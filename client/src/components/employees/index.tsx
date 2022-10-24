import axios from 'axios'
import { Component, Match, Switch } from 'solid-js'
import { createQuery } from '@tanstack/solid-query'
import { http } from 'common/clients'
import type { EmployeeType } from 'components'
import { CreateForm } from 'components'

const getEmployees = async () => {
  try {
    const response = await http.get<EmployeeType[]>('/tree')
    return response.data
  } catch (e) {
    if (axios.isAxiosError(e)) {
      console.error('* Axios error message: ', e.message)
    } else {
      console.error('* Unexpected error: ', e)
    }
  }
}

export const Employees: Component = () => {
  const query = createQuery(() => ['Get all employees'], getEmployees)

  return (
    <div
      style={{
        display: 'flex',
        gap: '1rem',
        'flex-wrap': 'wrap',
        'place-items': 'center',
        'align-items': 'center',
        'justify-content': 'space-evenly'
      }}
    >
      <div
        style={{
          display: 'flex',
          gap: '20px',
          'flex-direction': 'column'
        }}
      >
        <CreateForm />
      </div>
      <Switch>
        <Match when={query.isLoading}>
          <pre>Loading...</pre>
        </Match>
        <Match when={query.isError}>
          <pre>No employee.</pre>
        </Match>
        <Match when={query.isSuccess}>
          <pre>{JSON.stringify(query.data, null, 2)}</pre>
        </Match>
      </Switch>
    </div>
  )
}
