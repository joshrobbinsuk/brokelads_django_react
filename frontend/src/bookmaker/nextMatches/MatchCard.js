import React from "react";
import { Accordion, AccordionSummary, AccordionDetails } from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

import Card from "src/ui/Card";
import MatchRow from "src/ui/MatchRow";
import BetTable from "./BetTable";

const MatchCard = ({ match }) => {
  return (
    <Card>
      <Accordion>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <MatchRow {...match} />
        </AccordionSummary>
        <AccordionDetails>
          <BetTable {...match} />
        </AccordionDetails>
      </Accordion>
    </Card>
  );
};

export default MatchCard;
