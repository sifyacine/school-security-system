import {
  Box,
  Center,
  Text,
  Stack,
  List,
  ListItem,
  ListIcon,
  Button,
  useColorModeValue,
} from "@chakra-ui/react";
import { FaIdCard, FaGraduationCap, FaBell } from "react-icons/fa";
export default function Advantages() {
  return (
    <Box
      display={"flex"}
      flexWrap={"wrap"}
      justifyContent={"space-around"}
      width={"80vw"}
      margin={"auto"}
    >
      <Box
        maxW={"250px"}
        w={"full"}
        bg={useColorModeValue("white", "gray.800")}
        boxShadow={"2xl"}
        rounded={"md"}
        overflow={"hidden"}
      >
        <Box
          fontSize={"8em"}
          display={"grid"}
          placeItems={"center"}
          color={"orange.400"}
          w={"100%"}
        >
          <FaIdCard />
        </Box>
        <Text fontSize={"xl"} fontWeight={700} textAlign={'center'} py={'1em'}>
          Secure Access
        </Text>
        <Box
          bg={useColorModeValue("gray.50", "gray.900")}
          px={6}
          py={10}
          h={"100%"}
        >
          <Text>
            Our system provides a secure way for staff to access the school
            premises, ensuring that only authorized personnel are allowed on
            site.
          </Text>
        </Box>
      </Box>
      <Box
        maxW={"250px"}
        w={"full"}
        bg={useColorModeValue("white", "gray.800")}
        boxShadow={"2xl"}
        rounded={"md"}
        overflow={"hidden"}
      >
        <Box
          fontSize={"8em"}
          display={"grid"}
          placeItems={"center"}
          color={"orange.400"}
          w={"100%"}
        >
          <FaGraduationCap />
        </Box>
        <Text fontSize={"xl"} fontWeight={700} textAlign={'center'} py={'1em'}>
        Student Safety
        </Text>
        <Box
          bg={useColorModeValue("gray.50", "gray.900")}
          px={6}
          py={10}
          h={"100%"}
        >
          <Text>
          We understand that the safety of our students is of utmost importance. That's why our system includes features such as real-time attendance tracking and emergency response protocols to ensure that students are safe at all times.
          </Text>
        </Box>
      </Box>
      <Box
        maxW={"250px"}
        w={"full"}
        bg={useColorModeValue("white", "gray.800")}
        boxShadow={"2xl"}
        rounded={"md"}
        overflow={"hidden"}
        h={'100%'}
      >
        <Box
          fontSize={"8em"}
          display={"grid"}
          placeItems={"center"}
          color={"orange.400"}
          w={"100%"}
        >
          <FaBell />
        </Box>
        <Text fontSize={"xl"} fontWeight={700} textAlign={'center'} py={'1em'}>
        Emergency Response
        </Text>
        <Box bg={useColorModeValue("gray.50", "gray.900")} px={6} py={10}>
          <Text>
            In cases of emergency, our School Security System has a built-in
            response mechanism to quickly alert staff and authorities, ensuring
            a prompt and effective response to any situation
          </Text>
        </Box>
      </Box>
    </Box>
  );
}
