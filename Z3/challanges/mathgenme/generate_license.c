void generate_license(char *param_1)

{
  int local_58;
  int i;
  int c;
  char license [56];
  char *password;
  
  password = param_1;
  strlen(param_1);
  c = 0;
  for (i = 0; i < 12; i = i + 1) {
    license[c] = password[c] * 'B' + password[c + 1] * 'g' + password[c + 2] * 'Y' +
                 password[c + 3] * '!';
    license[c + 1] = password[c + 3] * '3' + password[c + 2] * -0x67 + password[c + 1] * -0x7d +
         password[c] * 'I';
    license[c + 2] =
         (char)((int)password[c + 2] << 3) + password[c] * '6' + password[c + 3] +
         password[c + 1] * 'q';
    license[c + 3] =
         password[c + 1] * 3 + password[c] * 119 + password[c + 3] * '\x17' +
         password[c + 2] * '\x19';
    c = c + 4;
  }
  printf("Here is your license key:\n");
  for (local_58 = 0; local_58 < 0x30; local_58 = local_58 + 1) {
    printf("%02hhx",license[local_58]);
  }
  return;
}