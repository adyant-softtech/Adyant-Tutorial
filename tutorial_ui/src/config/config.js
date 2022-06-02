import React from "react";

 //const baseURL = '/'
const baseURL = 'http://localhost:8000/'

const config = {
    apiBaseURL : `${baseURL}`,
    staticBaseURL : `${baseURL}/static/`,
    apiTimeout: 500000
}

export default config;