import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Box,
  Heading,
  TableContainer,
  Table,
  Thead,
  Tr,
  Th,
  Tbody,
  Td,
  Button,
} from "@chakra-ui/react";
import Search from "./Search";

export default function Attendance() {
  const [attendanceData, setAttendanceData] = useState([]);
  const [filteredAttendanceData, setFilteredAttendanceData] = useState([]);

  useEffect(() => {
    // Fetch attendance data from Django backend
    axios
      .get("http://localhost:8000/live_attendance/")
      .then((response) => {
        setAttendanceData(response.data);
        setFilteredAttendanceData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const handleSearchResults = (results) => {
    setFilteredAttendanceData(results);
  };

  const handleAttendanceSubmit = () => {
    // Make API call to trigger face recognition in the Django backend
    axios
      .post(
        "http://localhost:8000/live_attendance/submit_attendance/",
        null,
        {
          headers: {
            "X-CSRFToken": window.CSRF_TOKEN, // Set the CSRF token in the request headers
          },
        }
      )
      .then((response) => {
        // Handle success response if needed
        console.log(response.data);
        // Refresh the attendance data after face recognition is completed
        refreshAttendanceData();
      })
      .catch((error) => {
        // Handle error response if needed
        console.log(error);
      });
  };

  const refreshAttendanceData = () => {
    // Fetch updated attendance data from Django backend
    axios
      .get("http://localhost:8000/live_attendance/")
      .then((response) => {
        setAttendanceData(response.data);
        setFilteredAttendanceData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <Box w={"90%"} margin={"auto"} py={"5em"}>
      <Heading padding={"1em"}>Live Attendance Table</Heading>
      <Button
        margin={"0 2em"}
        padding={"2em 2em"}
        onClick={handleAttendanceSubmit}
      >
        Submit Attendance
      </Button>
      <Search users={attendanceData} setSearchResults={handleSearchResults} />

      <TableContainer maxH={"20em"} overflowY={"scroll"}>
        <Table variant="simple">
          <Thead>
            <Tr>
              <Th>Number</Th>
              <Th>Student Name</Th>
              <Th>ID Card Number</Th>
              <Th>Time in</Th>
              <Th>Time out</Th>
              <Th>Role</Th>
            </Tr>
          </Thead>
          <Tbody>
            {filteredAttendanceData.map((e) => (
              <Tr key={e.id}>
                <Td>{e.number}</Td>
                <Td>{e.full_name}</Td>
                <Td>{e.card_id}</Td>
                <Td>{e.time_in}</Td>
                <Td>{e.time_out}</Td>
                <Td>{e.is_staff ? "Staff" : "Student"}</Td>
              </Tr>
            ))}
          </Tbody>
        </Table>
      </TableContainer>
    </Box>
  );
}
