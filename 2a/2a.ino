void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial) {
    ;  // wait for serial port to connect. Needed for native USB port only
  }

  int u =  1;
  int r =  2;
  uint16_t n =  10;
  uint8_t buffer[1000];
  uint16_t size =  0;

  Serial.println(n);

  for (int i = 0; i < n; i++){
    int a = u * pow(r, i);
    Serial.println(a);
    int temp = a;
    int digits = 0;

    while (temp > 0) {
      temp /= 10;
      digits++;
    }
    size = size + digits;
    temp = a;
    for (int j = 0; j < digits; j++) {
      buffer[size - j -1] = temp % 10 + 48;
      temp /= 10;
    }

  }

  uint16_t s = checksumCalculator(buffer, size);

  Serial.println(s, HEX);
}

uint16_t checksumCalculator(uint8_t * data, uint16_t length){
   uint16_t curr_crc = 0x0000;
   uint8_t sum1 = (uint8_t) curr_crc;
   uint8_t sum2 = (uint8_t) (curr_crc >> 8);
   int index;
   for(index = 0; index < length; index = index+1){
    sum1 = (sum1 + data[index]) % 255;
    sum2 = (sum2 + sum1) % 255;
  }
   return (sum2 << 8) | sum1;
}



void loop() {
  // put your main code here, to run repeatedly:
}

