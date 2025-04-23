import React from 'react';
import './TaskDashboard.css';

const TaskDashboard = () => {
  // This is a placeholder for your existing task manager UI
  // We’ll enhance it in the next task
  return (
    <div className="dashboard-container">
      <h1>TASK MANAGER</h1>
      <button className="add-task-button">Add task</button>
      <div className="task-list">
        <div className="task-item">
          <button className="status-button completed">completed</button>
          <button className="status-button incompleted">incompleted</button>
        </div>
      </div>
    </div>
  );
};

export default TaskDashboard;