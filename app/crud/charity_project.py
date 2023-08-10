from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_charity_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession
    ) -> Optional[int]:
        charity_project = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return charity_project.scalars().first()

    async def get_charity_project_close_date(
        self,
        project_id: int,
        session: AsyncSession
    ):
        project_close_date = await session.execute(
            select(CharityProject.close_date).where(
                CharityProject.id == project_id
            )
        )
        return project_close_date.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[CharityProject]:
        charity_projects = await session.execute(
            select(
                self.model.id,
                self.model.name,
                self.model.description,
                self.model.create_date,
                self.model.close_date
            ).where(
                self.model.fully_invested.is_(True)
            ).order_by(self.model.close_date - self.model.create_date)
        )
        return charity_projects.all()

    async def get_charity_project_invested_amount(
        self,
        project_id: int,
        session: AsyncSession
    ):
        project_invested_amount = await session.execute(
            select(CharityProject.invested_amount).where(
                CharityProject.id == project_id
            )
        )
        return project_invested_amount.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)
