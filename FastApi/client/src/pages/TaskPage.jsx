import React, { useEffect } from 'react'
import { useTasks } from '../context/TasksContext'
import TaskCart from '../components/TaskCart';

function TaskPage() {
  const {getTasks, tasks} = useTasks()

  useEffect(() => {
    getTasks()
  }, [])

  return (
    <div className='grid grid-cols-3 gap-2'>
      {
        tasks.map((task) => {
          return <TaskCart key={task.id} task={task} />
        })
      }
    </div>
  )
}

export default TaskPage