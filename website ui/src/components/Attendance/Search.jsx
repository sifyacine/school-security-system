import { Input, Box } from "@chakra-ui/react";
import { useState } from "react";

export default function Search({ users, setSearchResults }) {
  const [searchValue, setSearchValue] = useState("");

  const handleSearchChange = (e) => {
    const searchInput = e.target.value;
    setSearchValue(searchInput);

    const filteredUsers = users.filter((user) => {
      const firstName = user.full_name ? user.full_name.toLowerCase() : "";
      const searchInputLower = searchInput.toLowerCase();
      return firstName.includes(searchInputLower);
    });

    setSearchResults(filteredUsers);
  };

  return (
    <Box display="flex" gap="3em" padding="2em 3em" alignItems="center">
      <Input
        type="text"
        placeholder="Search"
        value={searchValue}
        onChange={handleSearchChange}
      />
    </Box>
  );
}
