import React from "react";
import { CircularProgress, Stack } from "@mui/material";

const Loading = () => (
  <Stack sx={{ alignItems: "center" }}>
    <CircularProgress />
  </Stack>
);

export default Loading;
