import React from "react";
import { Container, Typography, Box, Button, Stack } from "@mui/material";

import { useFetchUserQuery } from "../bookmakerApi";
import { Loading, Error, UpdateCard } from "src/ui";

const MyAccount = ({ handleLogout }) => {
  const { data, isLoading, isError } = useFetchUserQuery();

  if (isLoading) {
    return <Loading />;
  }
  if (isError) {
    return <Error />;
  }
  const { email, balance } = data;

  return (
    <Container maxWidth="sm" sx={{ display: "flex", justifyContent: "center" }}>
      <Box>
        <Typography variant="h2">user: {email}</Typography>
        <Typography variant="h2">balance: £{balance}</Typography>
        <Stack sx={{ justifyContent: "center", px: 6 }}>
          <Button variant="outlined" onClick={handleLogout}>
            Logout
          </Button>
        </Stack>
        <UpdateCard />
      </Box>
    </Container>
  );
};

export default MyAccount;
