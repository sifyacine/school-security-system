import React, { useState } from "react";
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

  Select,
  Textarea,
} from "@chakra-ui/react";
import axios from "axios";

export default function AddStaff() {
  const [payload, setPayload] = useState({
    firstName: "",
    lastName: "",
    number: "",
    email: "",
    card_id: "",
    gender: "male",
    address: "",
  });

  const handleChange = (e, field) => {
    const value = e.target.value;
    setPayload((prevPayload) => {
      return {
        ...prevPayload,
        [field]: value,
      };
    });
  };

  const handleSubmit = async () => {
    try {
      await axios.post("/registering/add_staff/", payload);
      console.log("Staff added successfully");
      setPayload({
        firstName: "",
        lastName: "",
        number: "",
        email: "",
        card_id: "",
        gender: "male",
        address: "",
      });
    } catch (error) {
      console.error("Error adding staff", error);
    }
  };

  return (
    React.createElement(Flex, {
      minH: "100vh",
      align: "center",
      justify: "center",
      bg: useColorModeValue("gray.50", "gray.800")
    }, [
      React.createElement(Stack, {
        spacing: 8,
        mx: "auto",
        maxW: "lg",
        py: 12,
        px: 6,
        key: "stack"
      }, [
        React.createElement(Stack, {
          align: "center",
          key: "heading-stack"
        }, [
          React.createElement(Heading, {
            fontSize: "4xl",
            textAlign: "center",
            key: "heading"
          }, "Add Staff")
        ]),
        React.createElement(Box, {
          rounded: "lg",
          bg: useColorModeValue("white", "gray.700"),
          boxShadow: "lg",
          p: 8,
          key: "box"
        }, [
          React.createElement(Stack, {
            spacing: 4,
            key: "form-stack"
          }, [
            React.createElement(HStack, {
              key: "name-hstack"
            }, [
              React.createElement(Box, {
                key: "first-name-box"
              }, [
                React.createElement(FormControl, {
                  id: "firstName",
                  isRequired: true,
                  key: "first-name-form-control"
                }, [
                  React.createElement(FormLabel, {
                    key: "first-name-label"
                  }, "First Name"),
                  React.createElement(Input, {
                    type: "text",
                    onChange: (e) => {
                      handleChange(e, "firstName");
                    },
                    key: "first-name-input"
                  })
                ])
              ]),
              React.createElement(Box, {
                key: "last-name-box"
              }, [
                React.createElement(FormControl, {
                  id: "lastName",
                  isRequired: true,
                  key: "last-name-form-control"
                }, [
                  React.createElement(FormLabel, {
                    key: "last-name-label"
                  }, "Last Name"),
                  React.createElement(Input, {
                    type: "text",
                    onChange: (e) => {
                      handleChange(e, "lastName");
                    },
                    key: "last-name-input"
                  })
                ])
              ])
            ]),
            React.createElement(FormControl, {
              id: "number",
              isRequired: true,
              key: "number-form-control"
            }, [
              React.createElement(FormLabel, {
                key: "number-label"
              }, "Number"),
              React.createElement(Input, {
                type: "text",
                onChange: (e) => {
                  handleChange(e, "number");
                },
                key: "number-input"
              })
            ]),
            React.createElement(FormControl, {
              id: "email",
              isRequired: true,
              key: "email-form-control"
            }, [
              React.createElement(FormLabel, {
                key: "email-label"
              }, "Staff Email"),
              React.createElement(Input, {
                type: "email",
                onChange: (e) => {
                  handleChange(e, "email");
                },
                key: "email-input"
              })
            ]),
            React.createElement(FormControl, {
              id: "card_id",
              isRequired: true,
              key: "card-id-form-control"
            }, [
              React.createElement(FormLabel, {
                key: "card-id-label"
              }, "Card ID"),
              React.createElement(InputGroup, {
                key: "card-id-input-group"
              }, [
                React.createElement(Input, {
                  type: "text",
                  onChange: (e) => {
                    handleChange(e, "card_id");
                  },
                  key: "card-id-input"
                })
              ])
            ]),
            React.createElement(FormControl, {
              id: "gender",
              isRequired: true,
              key: "gender-form-control"
            }, [
              React.createElement(FormLabel, {
                key: "gender-label"
              }, "Gender"),
              React.createElement(Select, {
                defaultValue: "male",
                onChange: (e) => {
                  handleChange(e, "gender");
                },
                key: "gender-select"
              }, [
                React.createElement("option", {
                  value: "male",
                  key: "male-option"
                }, "male"),
                React.createElement("option", {
                  value: "female",
                  key: "female-option"
                }, "female")
              ])
            ]),
            React.createElement(FormControl, {
              id: "address",
              isRequired: true,
              key: "address-form-control"
            }, [
              React.createElement(FormLabel, {
                key: "address-label"
              }, "Address"),
              React.createElement(InputGroup, {
                key: "address-input-group"
              }, [
                React.createElement(Textarea, {
                  onChange: (e) => {
                    handleChange(e, "address");
                  },
                  key: "address-textarea"
                })
              ])
            ]),
            React.createElement(Stack, {
              spacing: 10,
              pt: 2,
              key: "button-stack"
            }, [
              React.createElement(Button, {
                loadingText: "Submitting",
                size: "lg",
                bg: "blue.400",
                color: "white",
                _hover: {
                  bg: "blue.500",
                },
                onClick: handleSubmit,
                key: "submit-button"
              }, "Submit")
            ])
          ])
        ])
      ])
    ])
  );
}
