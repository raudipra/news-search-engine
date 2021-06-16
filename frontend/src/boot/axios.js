import Vue from 'vue'
import axios from 'axios'

export const http = axios.create({
  baseURL: process.env.NEWS_API
})

Vue.prototype.$http = http
