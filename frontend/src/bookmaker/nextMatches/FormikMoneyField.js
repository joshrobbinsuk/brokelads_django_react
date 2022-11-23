import React from "react";
import { useField } from "formik";
import { TextField, InputAdornment, Typography } from "@mui/material";
import { useTheme } from "@mui/material/styles";

const FormikMoneyField = ({ helperText, ...props }) => {
  const theme = useTheme();
  const [field] = useField(props);
  return (
    <TextField
      {...field}
      {...props}
      sx={{
        "& .MuiFormHelperText-root": {
          color: theme.palette.red.main,
          fontSize: "14px",
        },
      }}
      InputProps={{
        startAdornment: (
          <InputAdornment position="start">
            <Typography
              sx={{
                color: theme.palette.darkGrey.main,
                position: "relative",
                top: "0.5px",
              }}
            >
              £
            </Typography>
          </InputAdornment>
        ),
      }}
      fullWidth
      type="number"
      variant="outlined"
      helperText={helperText}
    />
  );
};

export default FormikMoneyField;
