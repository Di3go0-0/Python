import { createContext, useState, useContext, useEffect } from "react";
import { RegisterRequest, LoginRequest } from "../api/auth";

export const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [errors, setErrors] = useState([]);

  const signup = async (user) => {
    try {
      const res = await RegisterRequest(user);
      console.log(res.data);
      setUser(res.data);
      setIsAuthenticated(true);
    } catch (e) {
      if (Array.isArray(e.response.data)) {
        console.log(e.response.data);
        return setErrors(e.response.data);
      }
      setErrors([e.response.data.message]);
      console.log(e.response.data.message);
    }
  };
  const singIn = async (user) => {
    try {
      const res = await LoginRequest(user);
      console.log(res.data);
    } catch (e) {
      if (Array.isArray(e.response.data)) {
        console.log(e.response.data);
        return setErrors(e.response.data);
      }
      setErrors([e.response.data.message]);
      console.log(e.response.data.message);
    }
  };

  useEffect(() => {
    if (errors.length > 0) {
      const timer = setTimeout(() => {
        setErrors([]);
      }, 5000);
      return () => clearTimeout(timer);
    }
  })

  return (
    <AuthContext.Provider
      value={{
        signup,
        singIn,
        user,
        isAuthenticated,
        errors,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
