import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  HStack,
  Stack,
  Button,
  Heading,
  useColorModeValue,
  Textarea,
} from "@chakra-ui/react";

const AddStudent = () => {
  const [payload, setPayload] = useState({
    firstName: "",
    lastName: "",
    card_id: "",
    fatherFirstName: "",
    fatherLastName: "",
    number: "",
    parentsEmail: "",
    address: "",
  });

  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setPayload((prevPayload) => {
      return { ...prevPayload, [name]: value };
    });
  };

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/registering/add_student/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        // Handle success response from the server if needed
        navigate("/dashboard"); // Redirect to the dashboard page
      })
      .catch((error) => {
        console.error("Error:", error);
        // Handle error response from the server if needed
      });
  };

  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Stack spacing={8} mx={"auto"} maxW={"lg"} py={12} px={6}>
        <Stack align={"center"}>
          <Heading fontSize={"4xl"} textAlign={"center"}>
            Add Student
          </Heading>
        </Stack>
        <Box
          rounded={"lg"}
          bg={useColorModeValue("white", "gray.700")}
          boxShadow={"lg"}
          p={8}
        >
          <Stack spacing={4}>
            <HStack>
              <Box>
                <FormControl id="firstName" isRequired>
                  <FormLabel>First Name</FormLabel>
                  <Input
                    type="text"
                    name="firstName"
                    onChange={handleChange}
                    value={payload.firstName}
                  />
                </FormControl>
              </Box>
              <Box>
                <FormControl id="lastName" isRequired>
                  <FormLabel>Last Name</FormLabel>
                  <Input
                    type="text"
                    name="lastName"
                    onChange={handleChange}
                    value={payload.lastName}
                  />
                </FormControl>
              </Box>
            </HStack>
            <FormControl id="card_id" isRequired>
              <FormLabel>Card ID</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  name="card_id"
                  onChange={handleChange}
                  value={payload.card_id}
                />
              </InputGroup>
            </FormControl>
            <HStack>
              <Box>
                <FormControl id="fatherFirstName" isRequired>
                  <FormLabel>Father First Name</FormLabel>
                  <Input
                    type="text"
                    name="fatherFirstName"
                    onChange={handleChange}
                    value={payload.fatherFirstName}
                  />
                </FormControl>
              </Box>
              <Box>
                <FormControl id="fatherLastName" isRequired>
                  <FormLabel>Father Last Name</FormLabel>
                  <Input
                    type="text"
                    name="fatherLastName"
                    onChange={handleChange}
                    value={payload.fatherLastName}
                  />
                </FormControl>
              </Box>
            </HStack>
            <FormControl id="number" isRequired>
              <FormLabel>Number</FormLabel>
              <Input
                type="text"
                name="number"
                onChange={handleChange}
                value={payload.number}
              />
            </FormControl>
            <FormControl id="parentsEmail" isRequired>
              <FormLabel>Parents Email</FormLabel>
              <Input
                type="email"
                name="parentsEmail"
                onChange={handleChange}
                value={payload.parentsEmail}
              />
            </FormControl>
            <FormControl id="address" isRequired>
              <FormLabel>Address</FormLabel>
              <InputGroup>
                <Textarea
                  name="address"
                  onChange={handleChange}
                  value={payload.address}
                />
              </InputGroup>
            </FormControl>
            <Stack spacing={10} pt={2}>
              <Button
                loadingText="Submitting"
                size="lg"
                bg={"blue.400"}
                color={"white"}
                _hover={{
                  bg: "blue.500",
                }}
                onClick={handleSubmit}
              >
                Submit
              </Button>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
};

export default AddStudent;
