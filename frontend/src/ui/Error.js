import React from "react";
import { Typography, Stack, Box } from "@mui/material";

const Loading = () => (
  <Stack sx={{ alignItems: "center" }}>
    <Box>
      <Typography variant="h2">
        Sorry, something's up at brokelads! If you're able to contact the
        helpdesk using the chat box, then please let us know what's up.
        Hopefully the issue will be fixed soon.
      </Typography>
    </Box>
  </Stack>
);

export default Loading;
