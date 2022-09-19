#include "sbus.h"

#define SBUS_MIDD_VAL 900
#define SBUS_MAX_VAL 1300
#define SBUS_MIN_VAL 500

#define ACC_INDEX 2
int32_t channelData[16];
uint8_t dataFlag = 0;
uint8_t loseFlag = 0;

void sbusDataHandler(uint8_t* sbusBuffer, uint16_t size)
{
    if(size < 24) {
        return;
    }

	if((sbusBuffer[0] == 0x0F) 
		&& (sbusBuffer[24] == 0x00)) {
		channelData[0] = ((sbusBuffer[1] | sbusBuffer[2] << 8) & 0x07FF);
		channelData[1] = ((sbusBuffer[2] >> 3 | sbusBuffer[3] << 5) & 0x07FF);
		channelData[2] = ((sbusBuffer[3] >> 6 | sbusBuffer[4] << 2 | sbusBuffer[5] << 10) & 0x07FF);
		channelData[3] = ((sbusBuffer[5] >> 1 | sbusBuffer[6] << 7) & 0x07FF);
		channelData[4] = ((sbusBuffer[6] >> 4 | sbusBuffer[7] << 4) & 0x07FF);
		channelData[5] = ((sbusBuffer[7] >> 7 | sbusBuffer[8] << 1 | sbusBuffer[9] << 9) & 0x07FF);
		channelData[6] = ((sbusBuffer[9] >> 2 | sbusBuffer[10] << 6) & 0x07FF);
		
        if((channelData[0] == 1001)
                && (channelData[1] == 1001)
                && (channelData[2] == 41)
                && (channelData[3] == 1001)) {
            loseFlag = 1;
        } else {
            loseFlag = 0;
        }

        dataFlag = 1;
	}
}

