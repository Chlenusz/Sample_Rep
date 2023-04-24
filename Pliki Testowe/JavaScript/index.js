function twiceAsOld(dadYearsOld, sonYearsOld) 
{
    if(dadYearsOld == sonYearsOld * 2)
    {
      return 0;
    }
    else if(dadYearsOld > sonYearsOld * 2)
    {
      for (let i=0;i<1000,i++;)
      {
        sonYearsOld +=i;
        number++;

        if(dadYearsOld > sonYearsOld * 2)
        {
            return 0;
        }
      }
    }

    else
    {
        return 0;
    }
  }



console.log(twiceAsOld(44, 21))
