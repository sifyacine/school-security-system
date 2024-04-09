import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home/Home';
import SignIn from './components/SignIn';
import Dashboard from './components/Dashboard/Dashboard';
import AddStaff from './components/Add/Staff/AddStaff'
import AddStudent from './components/Add/student/AddStudent';
import StaffReport from './components/Report/Staff/StaffReport';
import StudentReport from './components/Report/student/StudentReport';
import Attendance from './components/Attendance/Attendance';
import SignUp from './components/SignUp';
export default function RouteRoot() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/signin" element={<SignIn />} />
      <Route path="/signup" element={<SignUp />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/add/staff" element={<AddStaff />} />
      <Route path="/report/staff" element={<StaffReport />} />
      <Route path="/add/student" element={<AddStudent />} />
      <Route path="/report/student" element={<StudentReport />} />
      <Route path="/attendance" element={<Attendance />} />
      
    </Routes>
  );
}
