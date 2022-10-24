import axios from 'axios'
import { API_URL } from 'common/constants'

const createClient = (baseURL: string) => axios.create({ baseURL })

export const http = createClient(API_URL)
