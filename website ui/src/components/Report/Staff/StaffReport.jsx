import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  HStack,
  InputRightElement,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  Link,
  Select,
  Textarea,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { getUsers } from "../../api";
export default function StaffReport() {
  const [staff,setStaff] = useState([])
  const [payload, setPayload] = useState({
    staff: "",
    subject: "",
    message: "",
   
  });
useEffect(()=>{
  getUsers().then(json =>{
    setStaff(json.users)
  })
},[])
console.log(staff)
  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Stack
        spacing={8}
        mx={"auto"}
        w={{ base: "90%", lg: "60%" }}
        py={12}
        px={6}
      >
        <Stack align={"center"}>
          <Heading fontSize={"4xl"} textAlign={"center"}>
            Staff Report
          </Heading>
        </Stack>
        <Box
          rounded={"lg"}
          bg={useColorModeValue("white", "gray.700")}
          boxShadow={"lg"}
          p={8}
        >
          <Stack spacing={4}>
            <FormControl id="Staff" isRequired>
              <FormLabel>Staff</FormLabel>
              <Select
                onChange={(e) => {
                  setPayload({ ...payload, staff: staff[e.target.value] });
                }}
              >
               {staff.map((e,i)=>{return <option key={e.id} value={i}>{e.firstName}</option>})}
              </Select>
            </FormControl>
            <FormControl id="Subject" isRequired>
              <FormLabel>Subject</FormLabel>
              <Input
                type="text"
                onChange={(e) => {
                  setPayload({ ...payload, subject: e.target.value });
                }}
              />
            </FormControl>

            <FormControl id="address" isRequired>
              <FormLabel>Message</FormLabel>
              <InputGroup>
                <Textarea
                  onChange={(e) => {
                    setPayload({ ...payload, message: e.target.value });
                  }}
                ></Textarea>
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
                onClick={(e) => {
                  console.log(payload);
                }}
              >
                Submit
              </Button>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
}
