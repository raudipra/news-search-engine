import Vue from 'vue'
import axios from 'axios'

const headers = {
  'Access-Control-Allow-Origin': '*',
  'Content-Type': 'application/json'
}

export const http = axios.create({
  baseURL: process.env.NEWS_API,
  headers
})

Vue.prototype.$http = http
