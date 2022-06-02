import { Form, Input, Button, message } from 'antd';
import API from '../../api/API';
import { Authenticate } from '../../api/serviceApi'
import './index.css'

const Login = () =>{

    const onFinish = async(formData) =>{
        // const response = await API.post('tutorial/v1/api/auth', {}, {
        //   auth: {
        //     username: formData.username,
        //     password: formData.password
        //   }
        // }
        const response =  await Authenticate(data)
        try {
          if (response){
            let msg = `${response.username}  User Login Success`
            message.info(msg)
          }
          else{
            message.error('User Login not Success')
          }
        }
        catch(err){
          message.error('User Login not Success')
          return []
        }
        
    }

    return (
        <div style={{position: 'center'}}>          
        <Form
          className='login'
          name="basic"
          labelCol={{
            span: 8,
          }}
          wrapperCol={{
            span: 8,
          }}
          onFinish={onFinish}
        //   onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item
            label="Username"
            name="username"
            rules={[
              {
                required: true,
                message: 'Please input your username!',
              },
            ]}
          >
            <Input />
          </Form.Item>
    
          <Form.Item
            label="Password"
            name="password"
            rules={[
              {
                required: true,
                message: 'Please input your password!',
              },
            ]}
          >
            <Input.Password />
          </Form.Item>
        
          <Form.Item
            wrapperCol={{
              offset: 8,
              span: 8,
            }}
          >
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
        </div>
    );
}

export default Login;