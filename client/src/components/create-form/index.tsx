import { createMutation, useQueryClient } from '@tanstack/solid-query'
import axios from 'axios'
import { http } from 'common/clients'
import { EmployeeType } from 'components/employees/type'
import { Component, createSignal } from 'solid-js'

const createEmployee = async (payload: Omit<EmployeeType, 'id'>) => {
  try {
    const response = await http.post('/users', {
      name: payload.name,
      surname: payload.surname,
      salary: payload.salary,
      position: payload.position,
      boss_id: payload.boss_id
    })
    return response.data
  } catch (e) {
    if (axios.isAxiosError(e)) {
      console.error('* Axios error message: ', e.message)
    } else {
      console.error('* Unexpected error: ', e)
    }
  }
}

export const CreateForm: Component = () => {
  const queryClient = useQueryClient()
  const [formData, setFormData] = createSignal({
    name: '',
    surname: '',
    salary: 0,
    position: '',
    boss_id: undefined
  })

  const mutation = createMutation(createEmployee, {
    onSuccess: async () => {
      queryClient.invalidateQueries(['Get all employees'])
    }
  })

  const onChange = (e: any) =>
    setFormData({
      ...formData(),
      [e.target.name]: e.target.value
    })

  const onSubmit = (e: any) => {
    e.preventDefault()
    mutation.mutate(formData())
  }

  return (
    <form
      onsubmit={onSubmit}
      style={{
        padding: '20px',
        display: 'flex',
        gap: '10px',
        border: '1px solid black',
        'flex-direction': 'column',
        'border-radius': '1rem'
      }}
    >
      <h3>Create an employee</h3>
      <input
        onChange={onChange}
        name="name"
        type="text"
        value={formData().name}
        placeholder="Name"
        required
      />
      <input
        onChange={onChange}
        name="surname"
        type="text"
        value={formData().surname}
        placeholder="Surname"
        required
      />
      <input
        onChange={onChange}
        name="salary"
        type="text"
        value={formData().salary}
        placeholder="Salary"
        required
      />
      <input
        onChange={onChange}
        name="position"
        type="text"
        value={formData().position}
        placeholder="Position"
        required
      />
      <input
        onChange={onChange}
        name="boss_id"
        type="number"
        value={formData().boss_id}
        placeholder="Boss id (Optional)"
      />
      <button type="submit">Submit</button>
    </form>
  )
}
