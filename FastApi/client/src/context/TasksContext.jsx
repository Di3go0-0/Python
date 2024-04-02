import { createContext, useContext, useState } from "react";
import {
  createTaskRequest,
  getTasksRequest,
  taskToggleRequest,
  deleteTaskRequest,
  updateTaskRequest
} from "../api/tasks";

const TaskContext = createContext();

export const useTasks = () => {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error("useTasks must be used within a TaskProvider");
  }
  return context;
};

export function TaskProvider({ children }) {
  const [tasks, setTasks] = useState([]);

  const getTasks = async () => {
    try {
      const res = await getTasksRequest();
      setTasks(res.data);
      console.log(res.data);
    } catch (error) {
      console.log(error);
    }
  };



  const createTask = async (task) => {
    const res = await createTaskRequest(task);
    console.log(res);
  };

  const taskToggle = async (id) => {
    const res = await taskToggleRequest(id);
    console.log(res.status);
    if(res.status === 200) getTasks(tasks);
  };

  const deleteTask = async (id) => {
    try {
      const res = await deleteTaskRequest(id);
      console.log(res.status);
      if (res.status === 200) setTasks(tasks.filter((task) => task.id !== id));
    } catch (error) {
      console.log(error);
    }
  };

  const updateTask = async (task) => {
    try {
      const res = await updateTaskRequest(task);
      console.log(res.data);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <TaskContext.Provider
      value={{
        tasks,
        createTask,
        getTasks,
        taskToggle,
        deleteTask,
        updateTask,
      }}
    >
      {children}
    </TaskContext.Provider>
  );
}
