import React from "react";
import { Typography, Box } from "@mui/material";

import { useFetchServerWillRefreshQuery } from "src/bookmaker/bookmakerApi";

const UpdateCard = () => {
  const refresh = useFetchServerWillRefreshQuery(null, {
    pollingInterval: 60 * 1000,
  });
  return (
    <Box mt={4} sx={{ textAlign: "center" }}>
      <Typography variant="body2">
        Results next updated at {refresh.data?.nextRefresh}
      </Typography>
      <Typography variant="body2">
        Results last updated at {refresh.data?.lastRefresh}
      </Typography>
    </Box>
  );
};

export default UpdateCard;
