import axios from "axios";
const API = "http://localhost:3600";

export const registerRequest = (user) =>
  axios.post(`${API}/register`, user);
