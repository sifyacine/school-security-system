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
  Grid,
} from "@chakra-ui/react";
import { useState,useEffect } from "react";
import { ViewIcon, ViewOffIcon } from "@chakra-ui/icons";
import { getUsers } from "../../api";

export default function StudentReport() {
  const [staff,setStaff] = useState([])
  const [fileName, setfileName] = useState("");
  const [payload, setPayload] = useState({
    student: {},
    subject: "",
    attachment: {},
    message: "",
  });
  useEffect(()=>{
    getUsers().then(json =>{
      setStaff(json.users)
    })
  },[])
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
            Student Report
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
              <FormLabel>Student</FormLabel>
              <Select
                onChange={(e) => {
                  setPayload({ ...payload, student: staff[e.target.value]});
                }}
              >
               {staff.map((e,i)=>{return <option key={e.id} value={i}>{e.firstName}</option>})}
              </Select>
            </FormControl>
            <FormControl id="Subject" isRequired>
              <FormLabel>Repor title</FormLabel>
              <Input
                type="text"
                onChange={(e) => {
                  setPayload({ ...payload, subject: e.target.value });
                }}
              />
            </FormControl>

            <FormControl id="address" isRequired>
              <FormLabel>Report Content</FormLabel>
              <InputGroup>
                <Textarea
                  onChange={(e) => {
                    setPayload({ ...payload, message: e.target.value });
                  }}
                ></Textarea>
              </InputGroup>
            </FormControl>
            <FormControl id="address">
              <FormLabel>Attachment</FormLabel>
              <InputGroup>
                <Grid
                  gap={2}
                  templateColumns={{ lg: "1fr 3fr", base: "1fr" }}
                  w={"100%"}
                >
                  <label
                    htmlFor="pdf"
                    style={{
                      borderRadius: "5px",
                      border: "1px solid rgba(200,200,200,0.4)",
                      cursor: "pointer",
                      display: "grid",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    Import
                    <Input
                      id="pdf"
                      display={"none"}
                      placeholder="Upload"
                      type={"file"}
                      pt={"0.3em"}
                      onChange={(e) => {
                        setfileName(e.target.value);
                        setPayload({...payload,attachment : e.target.value})
                      }}
                    />
                  </label>
                  <Input
                    type="text"
                    readOnly
                    textAlign={"center"}
                    value={fileName.toString().substring(12, 1000)}
                  />
                </Grid>
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
