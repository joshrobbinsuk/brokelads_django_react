import React from "react";
import { Box, Stack, Typography } from "@mui/material";

import Card from "src/ui/Card";
import MatchRow from "src/ui/MatchRow";

const BetCard = ({ match, stake, returns, outcome, choice, ...rest }) => {
  return (
    <Card extraPadding>
      <MatchRow {...match} />
      <Stack mt={1} sx={{ alignItems: "center" }}>
        <Box>
          <Typography variant="body2">{`£${stake} ${choice}`}</Typography>
        </Box>
      </Stack>
    </Card>
  );
};

export default BetCard;
