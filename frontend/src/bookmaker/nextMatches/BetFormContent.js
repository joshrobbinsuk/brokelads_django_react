import { useFormikContext } from "formik";
import React, { useEffect } from "react";
import { Stack } from "@mui/material";

import FormikMoneyField from "./FormikMoneyField";

const PlaceBetFormContent = ({ odds, balance }) => {
  const {
    values: { stake },
    setFieldValue,
  } = useFormikContext();

  useEffect(() => {
    setFieldValue("returns", (stake * odds).toFixed(2));
  }, [stake, odds, setFieldValue]);
  return (
    <>
      <Stack direction="column">
        <FormikMoneyField
          name="stake"
          label="Your stake"
          helperText={`Your balance is £${balance}`}
        />
        <FormikMoneyField
          name="returns"
          label="Wins"
          disabled={true}
          helperText={null}
        />
      </Stack>
    </>
  );
};

export default PlaceBetFormContent;
