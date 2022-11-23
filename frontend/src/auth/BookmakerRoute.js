import React, { useState } from "react";
import { Amplify, Auth } from "aws-amplify";
import { Authenticator } from "@aws-amplify/ui-react";
import "@aws-amplify/ui-react/styles.css";
import { Stack, Box, Typography } from "@mui/material";

import config from "../config";
import Bookmaker from "src/bookmaker/Bookmaker";

Amplify.configure(config.cognito.customer);

const BookmakerRoute = () => {
  const handleSignIn = async (formData) => {
    const { username, password } = formData;
    return Auth.signIn({
      username,
      password,
    });
  };

  return (
    <Stack mt={15}>
      <Authenticator
        loginMechanisms={["email"]}
        components={{ Header }}
        services={{ handleSignIn }}
      >
        {({ signOut }) => <Bookmaker signOut={signOut} />}
      </Authenticator>
    </Stack>
  );
};

const Header = () => (
  <Box w={"100%"} sx={{ textAlign: "center" }}>
    <Typography variant="h1">BROKELADS</Typography>
  </Box>
);

export default BookmakerRoute;
