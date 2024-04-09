import React from "react";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter } from "react-router-dom";
import NavBar from "./components/NavBar";
import RouteRoot from "./Routes";
export default function App() {
  return (
    <ChakraProvider>
      <BrowserRouter>
      <NavBar />
      <RouteRoot/>
      </BrowserRouter>
     
    </ChakraProvider>
  );
}
