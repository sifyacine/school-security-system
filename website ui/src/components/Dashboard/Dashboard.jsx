import React, { useState, useEffect } from "react";
import {
  Box,
  Table,
  TableContainer,
  Th,
  Tr,
  Td,
  Thead,
  Tbody,
  Heading,
} from "@chakra-ui/react";
import Search from "./Search";
import axios from "axios";

export default function Dashboard() {
  const [students, setStudents] = useState([]);
  const [staff, setStaff] = useState([]);
  const [studentSearchResults, setStudentSearchResults] = useState([]);
  const [staffSearchResults, setStaffSearchResults] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get("/dashboard/student_list/");
        setStudents(response.data.students);
        setStaff(response.data.staff);
        setStudentSearchResults(response.data.students);
        setStaffSearchResults(response.data.staff);
      } catch (error) {
        console.error(error);
      }
    }
    fetchData();
  }, []);

  return (
    <>
      <Box w={"90%"} margin={"auto"} py={"5em"}>
        <Heading>Students Table</Heading>
        <Search users={students} setSearchResults={setStudentSearchResults} />
        <TableContainer maxH={"20em"} overflowY={"scroll"}>
          <Table variant="simple">
            <Thead>
              <Tr>
                <Th>Number</Th>
                <Th>Father Full Name</Th>
                <Th>Full Name</Th>
                <Th>ID Card Number</Th>
                <Th>Parents Email Address</Th>
                <Th>Address</Th>
              </Tr>
            </Thead>
            <Tbody>
              {studentSearchResults.map((e) => {
                return (
                  <Tr key={e.id}>
                    <Td>{e.number}</Td>
                    <Td>{e.father_full_name}</Td>
                    <Td>{e.full_name} </Td>
                    <Td>{e.card_id} </Td>
                    <Td>{e.parents_email} </Td>
                    <Td>{e.address} </Td>
                  </Tr>
                );
              })}
            </Tbody>
          </Table>
        </TableContainer>
      </Box>
      <Box w={"90%"} margin={"auto"} py={"5em"}>
        <Heading>Staff Table</Heading>
        <Search users={staff} setSearchResults={setStaffSearchResults} />
        <TableContainer maxH={"20em"} overflowY={"scroll"}>
          <Table variant="simple">
            <Thead>
              <Tr>
                <Th>Number</Th>
                <Th>Full Name</Th>
                <Th>ID Card Number</Th>
                <Th>Email Address</Th>
                <Th>Address</Th>
                <Th>Gender</Th>
              </Tr>
            </Thead>
            <Tbody>
              {staffSearchResults.map((e) => {
                return (
                  <Tr key={e.id}>
                    <Td>{e.number}</Td>
                    <Td>{e.full_name} </Td>
                    <Td>{e.card_id} </Td>
                    <Td>{e.staff_email} </Td>
                    <Td>{e.address} </Td>
                    <Td>{e.gender} </Td>
                  </Tr>
                );
              })}
            </Tbody>
          </Table>
        </TableContainer>
      </Box>
    </>
  );
}
