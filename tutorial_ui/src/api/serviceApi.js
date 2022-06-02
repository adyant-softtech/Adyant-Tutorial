import { message } from 'antd'
import API from './API'

export const Authenticate = async(formData) => {
    const response = await API.post(`/tutorial/v1/api/get-auth-token`, formData,
    {headers : {'Content-Type':'application/json'}}).catch(
        err => message.error('Failed to authenticate the user.')
    )
    console.log(response.data)
    return response ? response.data: {}
}

export const register = async(formData) =>{
    const response = await API.post(`/tutorial/v1/api/register`, formData,
    {headers : {'Content-Type':'application/json'}}).catch(
        err => message.error('registrattion failed.')
    )
    console.log(response.data)
    return response ? response.data: {}
}