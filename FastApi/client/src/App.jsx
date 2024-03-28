import {BrowserRouter, Routes, Route} from 'react-router-dom';
import 'tailwindcss/tailwind.css'
import RegisterPage from './pages/RegisterPage';
// Importa tus componentes aquí
// import HomePage from './pages/HomePage';
// import TaskPage from './pages/TaskPage';
// import AddTaskPage from './pages/AddTaskPage';
// import TaskDetailPage from './pages/TaskDetailPage';
// import ProfilePage from './pages/ProfilePage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<h1>Hola Mundo</h1>} />
        {/* <Route path="/login" element={<LoginPage />} /> */}
        <Route path="/register" element={<RegisterPage />} />
        {/* <Route path="/task" element={<TaskPage />} />
        <Route path="/add-task" element={<AddTaskPage />} />
        <Route path="/task/:id" element={<TaskDetailPage />} />
        <Route path="/profile" element={<ProfilePage />} /> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;